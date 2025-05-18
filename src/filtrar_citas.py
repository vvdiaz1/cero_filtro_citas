import os
import sys
import pandas as pd
import numpy as np
from collections import defaultdict
from datetime import datetime, date
import json
from typing import List, Union, Dict


def cargar_reglas(
        reglas_path:str =r"data\reglas.json"
        )->List[Dict[str, Union[int, str, bool]]]:
    """
    Carga las reglas de negocio desde un archivo JSON
    
    Args: 
    - reglas_path: Ruta al archivo JSON que contiene las reglas a procesar, toma por defecto la ruta data\reglas.json
    Returns: 
        Lista de diccionarios que contienen las reglas
    """
    try:
        with open(reglas_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: El archivo de reglas '{reglas_path}' no se encontró")
        return []
    except json.JSONDecodeError as e:
        print(f"Error: El archivo '{reglas_path}' es un JSON inválido, {e}")
        return []

def cargar_citas(
        citas_path:str =r"data\citas.json"
        )->List[Dict[str, Union[int, str, bool]]]:
    """
    Carga las citas consultadas desde un archivo JSON

    Args: 
    - citas_path: Ruta al archivo JSON que contiene las citas consultadas, toma por defecto la ruta data\citas.json
    Returns: 
        Lista de diccionarios que contienen las citas
    """
    try:
        with open(citas_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: El archivo de citas '{citas_path}' no se encontró")
        return []
    except json.JSONDecodeError as e:
        print(f"Error: El archivo '{citas_path}' es un JSON inválido, {e}")
        return []

def unica_version_activa(reglas:list)->None:
    """
    Revisa si en una lista de reglas, alguna de ellas tiene más de una version activa 
    
    Args: 
    - reglas: lista de reglas a revisar
    Returns: 
        No retorna nada, sólo imprime información sobre las reglas que pueden generar conflicto, si las hay
    """
    versiones_activas = defaultdict(list)
    for item in reglas:
        if item["activa"]:
            versiones_activas[item["id"]].append(item)
    conflictos = {id_: items[0]["regla"] for id_, items in versiones_activas.items() if len(items) > 1}

    if conflictos:
        print("Error: Las siguientes reglas tienen más de una versión activa:")
        for id_, regla in conflictos.items():
            print(f"ID: {id_} - Regla: {regla}")

def match_especialidad(
        condicion:Dict[str, Union[int, str, bool]],
        cita:Dict[str, Union[int, str, bool]]
        )->Union[bool, None]:
    """
    Verifica si la especialidad de la condición hace match con la del profesional de la cita, comparando tanto el ID como el nombre para revisar si hay coincidencia.
    
    Args: 
    - condicion: diccionario que representa la condición de la regla
    - cita: diccionario que representa la información de la cita del paciente
    Returns: 
        True si el id o el nombre de la especialidad coinciden, False en caso contrario.
        Devuelve None si no se encuentra la información en la condición.
    """
    match_id, match_nombre = None, None

    if condicion.get("especialidad", {}).get("id",None) is not None and cita.get("profesional",{}).get("especialidad",{}).get("id",None) is not None:
        match_id = condicion.get("especialidad",{}).get("id",None)==cita.get("profesional",{}).get("especialidad",{}).get("id",None)

    if condicion.get("especialidad",{}).get("nombre",None) is not None and cita.get("profesional",{}).get("especialidad",{}).get("nombre",None) is not None:
        match_nombre = condicion.get("especialidad",{}).get("nombre")==cita.get("profesional",{}).get("especialidad",{}).get("nombre",None)

    return match_id or match_nombre

def match_profesional(
        condicion:Dict[str, Union[int, str, bool]],
        cita:Dict[str, Union[int, str, bool]]
        )->Union[bool, None]:
    """
    Verifica si el profesional de la condición hace match con el profesional de la cita, comparando tanto el ID como el rut para revisar si hay coincidencia.
    
    Args: 
    - condicion: diccionario que representa la condición de la regla
    - cita: diccionario que representa la información de la cita del paciente
    Returns: 
        True si el id o el rut del profesional coinciden, False en caso contrario.
        Devuelve None si no se encuentra la información en la condición.
    """
    match_id, match_rut = None, None

    if condicion.get("profesional", {}).get("id",None) is not None and cita.get("profesional",{}).get("especialidad",{}).get("id",None) is not None:
        match_id = condicion.get("profesional",{}).get("id",None)==cita.get("profesional",{}).get("especialidad",{}).get("id",None)

    if condicion.get("especialidad",{}).get("rut",None) is not None and cita.get("profesional",{}).get("especialidad",{}).get("rut",None) is not None:
        match_rut = condicion.get("profesional",{}).get("rut",None)==cita.get("profesional",{}).get("especialidad",{}).get("rut",None)
 
    return match_id or match_rut

def get_edad(
        fecha_nacimiento: str, 
        hoy:str = date.today().strftime('%Y-%m-%d')
        )->Union[int, None]:
    """
    Calcula la edad del paciente, revisando la diferencia de años entre hoy y la fecha de naciemiento. Descontando un año si el paciente aun no esta de cumpleaños este año.

    Args: 
    - fecha_nacimiento: string que contiene la fecha de naciemiento del paciente en formato YYYY-mm-dd
    - hoy: string que contiene el día que se considera como el actual(hoy) en caso de que se quieran revisar fechas ficticias, con formato YYYY-MM-DD
    Returns: 
        Devuelve un entero(int) con la edad del paciente en años y None si la fecha de nacimiento no es del tipo correcto.
    """
    if fecha_nacimiento is not None:
        fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()
        hoy = datetime.strptime(hoy, "%Y-%m-%d").date()
        edad = hoy.year - fecha_nacimiento.year
        if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
            edad -= 1  
        return edad
    return None

def is_lista_espera(
        cita:Dict[str, Union[int, str, bool]]
        )->bool:
    """
    Verifica si la atención corresponde a lista de espera
    
    Args: 
    - cita: diccionario que representa la información de la cita del paciente
    Returns: 
        True si el la atención corresponde a lista de espera, False en caso contrario.
    """
    return cita.get("atencion", {}).get("lista",None) == "lista de espera"

def is_tecera_edad(
        cita:Dict[str, Union[int, str, bool]],
        hoy:str = date.today().strftime('%Y-%m-%d')
        )->Union[int, None]:
    """
    Verifica si el paciente es de la tercera edad, considerando a mujeres (F) con edad mayor o igual a 60 años y a hombres (M) con edad mayor o igual a 65 años

    Args: 
    - cita: diccionario que representa la información de la cita del paciente
    - hoy: string que contiene el día que se considera como el actual(hoy) en caso de que se quieran revisar fechas ficticias, con formato YYYY-MM-DD
    Returns: 
        True si el paciente es de la tercera edad, False en caso contrario.
        Devuelve None si no se encuentra la información en la condición. 
    """
    if cita.get("paciente",{}).get("fecha_nacimiento",None) is not None:
        fecha_nacimiento = cita.get("paciente",{}).get("fecha_nacimiento",None)
        sexo = cita.get("paciente",{}).get("sexo",None)
        edad = get_edad(fecha_nacimiento,hoy)
        if sexo =='F' and edad>=60:
            return True
        elif sexo == "M" and edad>=65:
            return True
        return False
    return None

def match_tercera_edad(
        condicion:Dict[str, Union[int, str, bool]],
        cita:Dict[str, Union[int, str, bool]],
        hoy:str = date.today().strftime('%Y-%m-%d')
        )->Union[bool, None]:
    """
    Verifica si el paciente es de la tercera edad y si esto hace match con lo indicado en la condición
    
    Args: 
    - condicion: diccionario que representa la condición de la regla
    - cita: diccionario que representa la información de la cita del paciente
    - hoy: string que contiene el día que se considera como el actual(hoy) en caso de que se quieran revisar fechas ficticias, con formato YYYY-MM-DD
    Returns:
        True si la condición de tercera edad hace match, False en caso contrario.
        Devuelve None si no se encuentra la información en la condición.
    """
    if condicion.get('tercera_edad',None) is not None:
        return condicion.get('tercera_edad',None)==is_tecera_edad(cita,hoy)

def match_tipo_lista(
        condicion:Dict[str, Union[int, str, bool]],
        cita:Dict[str, Union[int, str, bool]]        
        )->Union[bool, None]:
    """
    Verifica si la atención corresponde a lista de espera y si esto hace match con lo indicado en la condición
    
    Args: 
    - condicion: diccionario que representa la condición de la regla
    - cita: diccionario que representa la información de la cita del paciente
    Returns:
        True si la condición de lista de espera hace match, False en caso contrario.
        Devuelve None si no se encuentra la información en la condición.
    """
    if condicion.get('lista_espera',None) is not None:
        return condicion.get('lista_espera',None)==is_lista_espera(cita)


def match_tipo_atencion(
        condicion:Dict[str, Union[int, str, bool]],
        cita:Dict[str, Union[int, str, bool]]        
        )->Union[bool, None]:
    """
    Verifica el tipo de atención de la cita y si esto hace match con lo indicado en la condición
    
    Args: 
    - condicion: diccionario que representa la condición de la regla
    - cita: diccionario que representa la información de la cita del paciente
    Returns:
        True si tipo de atención de la cita hace match con la condición, False en caso contrario.
        Devuelve None si no se encuentra la información en la condición.
    """
    if condicion.get('atencion',{}).get("tipo",None) is not None:
        return condicion.get('atencion',{}).get("tipo",None)==cita.get("atencion",{}).get("tipo",None)

def match_unidad_medica(
        condicion:Dict[str, Union[int, str, bool]],
        cita:Dict[str, Union[int, str, bool]]        
        )->Union[bool, None]:
    """
    Verifica unidad médica de la cita y si esto hace match con lo indicado en la condición
    
    Args: 
    - condicion: diccionario que representa la condición de la regla
    - cita: diccionario que representa la información de la cita del paciente
    Returns:
        True si la unidad médica de la cita hace match con la condición, False en caso contrario.
        Devuelve None si no se encuentra la información en la condición.
    """
    match_id, match_nombre = None, None

    if condicion.get("unidad_medica", {}).get("id",None) is not None and cita.get("unidad_medica",{}).get("id",None) is not None:
        match_id = condicion.get("unidad_medica",{}).get("id",None)==cita.get("unidad_medica",{}).get("id",None)

    if condicion.get("unidad_medica",{}).get("nombre",None) is not None and cita.get("unidad_medica",{}).get("nombre",None):
        match_nombre = condicion.get("unidad_medica",{}).get("nombre",None)==cita.get("unidad_medica",{}).get("nombre",None)

    return match_id or match_nombre

def match_estado(
        condicion:Dict[str, Union[int, str, bool]],
        cita:Dict[str, Union[int, str, bool]]        
        )->Union[bool, None]:
    """
    Verifica el estado de la cita y si esto hace match con lo indicado en la condición
    
    Args: 
    - condicion: diccionario que representa la condición de la regla
    - cita: diccionario que representa la información de la cita del paciente
    Returns:
        True si el estado de la cita hace match con la condición, False en caso contrario.
        Devuelve None si no se encuentra la información en la condición.
    """
    match_id, match_nombre = None, None

    if condicion.get("estado", {}).get("id",None) is not None and cita.get("estado",{}).get("id",None) is not None:
        match_id = condicion.get("estado",{}).get("id",None)==cita.get("estado",{}).get("id",None)

    if condicion.get("estado",{}).get("nombre",None) is not None and cita.get("estado",{}).get("nombre",None):
        match_nombre = condicion.get("estado",{}).get("nombre",None)==cita.get("estado",{}).get("nombre",None)

    return match_id or match_nombre

def dias_hasta_cita(
        fecha_hora:str,
        hoy:str = date.today().strftime('%Y-%m-%d')
        )->Union[bool, None]:
    """
    Calcula la cantidad de días que faltan para la cita del paciente
    
    Args: 
    - fecha_hora: string que contiene la fecha y hora de la cita del paciente
    - hoy: string que contiene el día que se considera como el actual(hoy) en caso de que se quieran revisar fechas ficticias, con formato YYYY-MM-DD
    Returns:
        Devuelve un entero(int) la cantidad de días que faltan para la cita del paciente y None si la fecha_hora de la cita no es del tipo correcto.
    """
    if fecha_hora is not None:
        fecha_hora = datetime.strptime(fecha_hora, '%Y-%m-%d %H:%M').date()
        hoy = datetime.strptime(hoy, "%Y-%m-%d").date()
        return(fecha_hora-hoy).days
    return None

def match_dias_antes(condicion,cita,hoy:str = date.today().strftime('%Y-%m-%d')):
    #se asume que si no viene la cantidad de dias antes para contactar se tiene que hacer a 1 dia de la cita 
    #es decir el dia antes de esta
    if condicion.get('dias_antes',None) is not None and cita.get("fecha_hora", None)is not None:
        fecha_hora =cita.get("fecha_hora", None)
        return condicion.get('dias_antes',None)==dias_hasta_cita(fecha_hora,hoy)
    elif condicion.get('dias_antes',None) is None and cita.get("fecha_hora", None) is not None:
        dias_antes_default = 1
        return dias_antes_default ==dias_hasta_cita(fecha_hora,hoy)


def condicion_match(condicion, cita,hoy:str = date.today().strftime('%Y-%m-%d')):
    checks = [
        match_especialidad(condicion, cita),
        match_profesional(condicion, cita),
        match_tipo_lista(condicion, cita),
        match_tipo_atencion(condicion, cita),
        match_unidad_medica(condicion, cita),
        match_estado(condicion, cita), 
        match_tercera_edad(condicion,cita,hoy),
        match_dias_antes(condicion,cita, hoy)
    ]
    return all(c in (True, None) for c in checks)

def contactar_cita(
        cita:Dict[str, Union[int, str, bool]],
        reglas:List[Dict[str, Union[int, str, bool]]], 
        hoy:str = date.today().strftime('%Y-%m-%d')
    )->Union[bool,None]:
    for regla in reglas:
        if regla.get("activa")==True:
            checks = []
            for condicion in regla.get("condiciones"):
                if condicion.get("enviar_mensaje",None) == True:
                    checks.append(condicion_match(condicion, cita, hoy))
            return any(c in (True, None) for c in checks)

# def filtrar_citas(
#         citas:List[Dict[str, Union[int, str, bool]]],
#         reglas:List[Dict[str, Union[int, str, bool]]], 
#         hoy:str = date.today().strftime('%Y-%m-%d')
#     )->List[Dict[str, Union[int, str, bool]]]:
#     filtro_citas:list = []
#     for cita in citas:
#         filtro_citas.append(contactar_cita(cita,reglas, hoy))

def filtrar_citas_para_contactar(
        citas: List[Dict[str, Union[int, str, bool]]],
        reglas: List[Dict[str, Union[int, str, bool]]],
        hoy: str = date.today().strftime('%Y-%m-%d')
    ) -> List[Dict[str, Union[int, str, bool]]]:
    """
    Filtra las citas que cumplen al menos una condición de una regla activa con `enviar_mensaje=True`.

    Args:
    - citas: Lista de diccionarios que contienen la información de la cita del paciente
    - reglas: Lista de diccionarios que representan las reglas de la institucion
    - hoy: string que contiene el día que se considera como el actual(hoy) en caso de que se quieran revisar fechas ficticias, con formato YYYY-MM-DD

    Returns:
    Lista de citas que cumplen con alguna condición para ser contactadas.
    """
    return [cita for cita in citas if contactar_cita(cita, reglas, hoy)]
    
    
def main():
    abspath = os.path.abspath(__file__)
    dirname = os.path.dirname(os.path.dirname(abspath))
    data_folder = os.path.join(dirname, 'data')
    reglas_path = os.path.join(data_folder, 'reglas.json')
    citas_path = os.path.join(data_folder, 'citas.json')

    citas_filtradas_path = os.path.join(data_folder, 'citas_filtradas.json')
    reglas:dict = cargar_reglas(reglas_path=reglas_path)
    citas:dict = cargar_citas(citas_path=citas_path)
    
    hoy_str:str = str(input("Ingrese la fecha actual (YYYY-MM-DD): "))
    try:
        datetime.strptime(hoy_str, '%Y-%m-%d')
        hoy:str = hoy_str
    except ValueError:
        print(f"Formato de fecha inválido. Usando la fecha por defecto: {date.today().strftime('%Y-%m-%d')}")
        hoy:str = date.today().strftime('%Y-%m-%d')

    output:list = filtrar_citas_para_contactar(citas, reglas, hoy)
    with open(citas_filtradas_path, 'w') as json_file:
        json.dump(output, json_file, indent=3)
    

if __name__ == "__main__":
    main()
    