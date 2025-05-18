#este script crea un citas.json con info dummy para recrear el output del modulo consultar_citas
#en base a una planilla de google sheets para poder recrear distintos escenarios en las pruebas
#y no tener que estar modificando manualmente el json de data dummy
import pandas as pd
import json
import os

def get_value(row, key):
    try:
        value = row[key]
        if pd.isna(value):
            return None
        return value
    except KeyError:
        return None

def create_consultar_citas_json(df: pd.DataFrame, schema: dict) -> list:
    output_json = []
    for _, row in df.iterrows():
        row_json = {}
        for key, value in schema.items():
            if isinstance(value, str):
                row_json[key] = get_value(row, value)
            elif isinstance(value, dict):
                nested_dict = {}
                for nested_key, nested_value in value.items():
                    if isinstance(nested_value, str):
                        nested_dict[nested_key] = get_value(row, nested_value)
                    elif isinstance(nested_value, dict):
                        inner_nested_dict = {}
                        for inner_key, inner_value in nested_value.items():
                            inner_nested_dict[inner_key] = get_value(row, inner_value)
                        nested_dict[nested_key] = inner_nested_dict
                row_json[key] = nested_dict
        output_json.append(row_json)
    return output_json


schema = {
    "id": "id",
    "extraction_timestamp": "extraction_timestamp",
    "fecha_hora": "fecha_hora",
    "atencion": {
        "id": "id_tipo_atencion",
        "tipo": "nombre_tipo_atencion",
        "lista":"tipo_lista",
        "categoria": "cat_tipo_atencion",
    },
    "unidad_medica": {
        "id": "id_unidad_medica",
        "nombre": "nombre_unidad_medica"
    },
    "estado": {
        "id": "id_estado",
        "nombre": "nombre_estado"
    },
    "profesional": {
        "id": "m_id",
        "rut": "m_rut",
        "nombre": "m_nombre",
        "apellido": "m_apellido",
        "especialidad": {
            "id": "m_id_especialidad",
            "nombre": "m_nombre_especialidad"
        },
        "institucion": {
            "id": "i_id",
            "nombre": "i_nombre"
        }
    },
    "paciente": {
        "id": "p_id",
        "rut": "p_rut",
        "nombre": "p_nombre",
        "apellido": "p_apellido",
        "sexo": "p_genero",
        "fecha_nacimiento": "p_fecha_nacimiento",
        "telefono": "p_telefono"
    }
}

sheets_url = "https://docs.google.com/spreadsheets/d/1-4MUM3TyGO5rbDo-2fgphXoW_vvNZk96oqJJeMRglmI/export?format=csv"

def main():
    abspath = os.path.abspath(__file__)
    dirname = os.path.dirname(os.path.dirname(abspath))
    data_folder = os.path.join(dirname, 'data')
    citas_path = os.path.join(data_folder, 'citas.json')
    
    df = pd.read_csv(sheets_url)
    output = create_consultar_citas_json(df, schema)
    with open(citas_path, 'w') as json_file:
        json.dump(output, json_file, indent=3)

if __name__ == "__main__":
    main()
