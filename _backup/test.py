import os

print("__file__:", __file__)
print("Absolute path:", os.path.abspath(__file__))



# reglas=[cargar_reglas(reglas_path =r"data\reglas.json")[0]]
# citas=cargar_citas(citas_path =r"data\citas.json")
# filter_ids = [14234, 14338, 14083, 14357, 14043, 14100, 14972, 14155, 14055, 14933, 14298, 14726, 14131]
# # filter_ids = [14338]
# # filter_ids = [14372, 14096, 14905]
# citas = [cita for cita in citas if cita['id'] in filter_ids]

# regla=reglas[0]
# # for condicion in regla.get("condiciones",[]):
# #     print(condicion)

# #validador
# hoy='2025-05-21'
# for cita in citas:
#     # dias_hasta_cita(cita)
#     # dias_hasta_cita(cita, hoy='2025-05-22')
#     # print(json.dumps(cita,indent=3))
#     print("id: ",cita.get("id",{}))
#     print("especialidad: ",cita.get("profesional",{}).get("especialidad",{}).get("nombre"))
#     print("profesional: ",cita.get("profesional",{}).get("apellido"))
#     print("tipo_lista: ",cita.get("atencion",{}).get("lista"))
#     print("atencion: ",cita.get("atencion",{}).get("tipo"))
#     print("estado: ",cita.get("estado",{}).get("nombre"))
#     print("edad: ", get_edad(cita.get("paciente",{}).get("fecha_nacimiento",None), hoy))
#     print("dias_hasta_cita: ",dias_hasta_cita(cita.get("fecha_hora", None),hoy))
#     print("hoy: ",hoy, " - fecha_hora: ",cita.get("fecha_hora", None))
#     print("contactar_cita: ",contactar_cita(cita,reglas, hoy))
#     print("-"*20)
#     for condicion in regla.get("condiciones",[]):
#         print("regla: ",regla.get("regla"))
#         print("match_especialidad: ",match_especialidad(condicion,cita)) #cardio
#         print("match_profesional: ",match_profesional(condicion,cita))
#         print("match_tipo_lista: ",match_tipo_lista(condicion,cita))
#         print("match_tipo_atencion: ",match_tipo_atencion(condicion,cita))#diagnostico
#         print("match_unidad_medica: ",match_unidad_medica(condicion,cita))
#         print("match_estado: ",match_estado(condicion,cita))
#         print("match_tercera_edad: ",match_tercera_edad(condicion, cita,hoy))
#         print("match_dias_antes: ",match_dias_antes(condicion,cita, hoy))#dias
#         print("----- FIN CONDICION -----")
#     print("-"*50)
#     print("-"*50)

# for cita in citas:    
#     print("id: ",cita.get("id",{}), " - ",contactar_cita(cita,reglas, hoy))


# print(match_especialidad(condicion,citas[0]))

# cita

# regla= reglas[2]
# cita=citas[1]


# for condicion in r.get("condiciones"):

#     # if isinstance(value, str):
#     print(condicion)

# def get_especialidad():
#     def es_de_especialidad(especialidad: str) -> Callable[[Dict], bool]:
#     return lambda cita: cita.get("especialidad") == especialidad


# def filtrar_citas(citas, reglas):
#     """Filtra la lista de citas según las reglas de negocio"""
#     citas_filtradas = []
#     for regla in reglas:
#         for cita in citas:
#             if evaluar_regla(cita, regla['condiciones']):
#                 cita['razon_filtrado'] = regla.get('descripcion')
#                 citas_filtradas.append(cita)
#     return citas_filtradas

# def evaluar_regla(cita, condiciones):
#     """Evalúa si una cita cumple con todas las condiciones de una regla"""
#     for condicion in condiciones:
#         campo = condicion['campo']
#         operador = condicion['operador']
#         valor = condicion['valor']

#         if campo not in cita:
#             return False  # El campo no existe en la cita

#         valor_cita = cita[campo]

#         if operador == 'igual' and valor_cita != valor:
#             return False
#         elif operador == 'distinto' and valor_cita == valor:
#             return False
#         elif operador == 'mayor_que' and valor_cita <= valor:
#             return False
#         elif operador == 'menor_que' and valor_cita >= valor:
#             return False
#         elif operador == 'contiene' and valor not in valor_cita:
#             return False
#         elif operador == 'no_contiene' and valor in valor_cita:
#             return False
#         elif operador == 'fecha_es_dentro_de_dias':
#             fecha_cita = datetime.strptime(cita['fecha_hora'].split(' ')[0], '%Y-%m-%d').date()
#             fecha_objetivo = datetime.now().date() + timedelta(days=valor)
#             if fecha_cita != fecha_objetivo:
#                 return False
#         # Agrega más operadores según sea necesario
#     return True

# if __name__ == "__main__":
#     # Ejemplo de datos de citas (simulando la salida del módulo "consultar citas")
#     citas_programadas = [
#         {'id_cita': 1, 'fecha_hora': '2025-05-18 10:00', 'especialidad': 'gastroenterología', 'tipo_atencion': 'primera vez', 'rut_medico': '12345678-9', 'nombre_medico': 'Dra. Ana Pérez', 'unidad_medica': 'gastroenterología', 'estado': 'agendada'},
#         {'id_cita': 2, 'fecha_hora': '2025-05-17 14:30', 'especialidad': 'cardiología', 'tipo_atencion': 'control', 'rut_medico': '98765432-1', 'nombre_medico': 'Dr. Luis Martínez', 'unidad_medica': 'cardiología', 'estado': 'confirmada'},
#         {'id_cita': 3, 'fecha_hora': '2025-05-18 09:00', 'especialidad': 'pediatría', 'tipo_atencion': 'control', 'rut_medico': '55555555-5', 'nombre_medico': 'Dra. Elena Gómez', 'unidad_medica': 'pediatría', 'estado': 'agendada', 'edad_paciente': 7},
#         {'id_cita': 4, 'fecha_hora': '2025-05-19 11:15', 'especialidad': 'cardiología', 'tipo_atencion': 'primera vez', 'rut_medico': '98765432-1', 'nombre_medico': 'Dr. Luis Martínez', 'unidad_medica': 'cardiología', 'estado': 'agendada', 'edad_paciente': 70},
#         {'id_cita': 5, 'fecha_hora': '2025-05-20 16:00', 'especialidad': 'gastroenterología', 'tipo_atencion': 'control', 'rut_medico': '12345678-9', 'nombre_medico': 'Dra. Ana Pérez', 'unidad_medica': 'gastroenterología', 'estado': 'confirmada'},
#     ]

#     # Ejemplo de archivo de reglas (reglas.json)
#     # [
#     #     {
#     #         "id": "regla_gastro_3dias_antes",
#     #         "descripcion": "Contactar pacientes de gastroenterología 3 días antes",
#     #         "condiciones": [
#     #             {"campo": "especialidad", "operador": "igual", "valor": "gastroenterología"},
#     #             {"campo": "fecha_es_dentro_de_dias", "operador": "igual", "valor": 3}
#     #         ]
#     #     },
#     #     {
#     #         "id": "regla_dr_martinez_dia_previo",
#     #         "descripcion": "Contactar pacientes del Dr. Martínez el día previo",
#     #         "condiciones": [
#     #             {"campo": "nombre_medico", "operador": "igual", "valor": "Dr. Luis Martínez"},
#     #             {"campo": "fecha_es_dentro_de_dias", "operador": "igual", "valor": 1}
#     #         ]
#     #     }
#     # ]

#     reglas_de_negocio = cargar_reglas("reglas.json")
#     if reglas_de_negocio:
#         citas_a_notificar = filtrar_citas(citas_programadas, reglas_de_negocio)
#         print("\nCitas que cumplen con las reglas:")
#         for cita in citas_a_notificar:
#             print(f"- ID: {cita['id_cita']}, Especialidad: {cita['especialidad']}, Fecha: {cita['fecha_hora']}, Razón: {cita['razon_filtrado']}")