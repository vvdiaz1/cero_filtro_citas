## Estructura Ejemplo de Inputs 🏗️

A continuación, se muestran a manera de ejemplo la estructura te los archivos citas.json y reglas.json que recibe el módulo. 

De igual forma dentro de la carpeta [docs/json_templates](/docs/json_templates) encontaras archivos de ejemplo.

### citas.json

```json
[
   {
      "id": 14338,
      "extraction_timestamp": "2025-05-16 12:23",
      "fecha_hora": "2025-05-27 17:15",
      "atencion": {
         "id": 2,
         "tipo": "control",
         "lista": "lista de espera",
         "categoria": "cita medica"
      },
      "unidad_medica": {
         "id": 30,
         "nombre": "Edificio B"
      },
      "estado": {
         "id": 1,
         "nombre": "agendada"
      },
      "profesional": {
         "id": 192,
         "rut": "5987654-K",
         "nombre": "Luis Alberto",
         "apellido": "Martinez",
         "especialidad": {
            "id": 3,
            "nombre": "cardiologia"
         },
         "institucion": {
            "id": 2017,
            "nombre": "Hospital Cero"
         }
      },
      "paciente": {
         "id": 1516,
         "rut": "10567890-1",
         "nombre": "Cristobal",
         "apellido": "Soto",
         "sexo": "M",
         "fecha_nacimiento": "1954-10-04",
         "telefono": 56967808123
      }
   }
]
```
### reglas.json

```json
[
    { 
        "id": 1,
        "activa":true,
        "version":1,
        "fecha_modificacion":"2025-05-17",
        "regla": "nombre_regla",
        "descripcion": "Descripcion de regla de negocio",
        "institucion": {
            "id": 2017,
            "nombre":"Hospital Cero"
        }, 
        "condiciones": [
            {   
                "enviar_mensaje": true,
                "especialidad": {
                    "nombre": "cardiologia"
                },
                "atencion": {
                    "tipo":"diagnostico"
                },
                "profesional": {
                    "rut": "5987654-K",
                    "apellido": "Martinez"
                },
                "estado": {
                    "nombre":"agendada"
                },
                "atencion": {
                    "tipo":"control"
                },
                "lista_espera":false,
                "tercera_edad": false,
                "dias_antes": 2
            },
            {
                "enviar_mensaje":true,
                "especialidad": {
                    "nombre": "cardiologia"
                },
                "atencion": {
                    "tipo":"control"
                },
                "dias_antes":0
            },
            {
                "enviar_mensaje":false,
                "especialidad": {
                    "nombre": "cardiologia"
                },
                "atencion": {
                    "tipo":"diagnostico"
                },
                "dias_antes":0
            }
        ]
    }
]
```