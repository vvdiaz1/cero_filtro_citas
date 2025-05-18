
# Filtros de citas médicas 🏥

Este proyecto tiene como objetivo principal construir un sistema flexible y dinámico para determinar si se debe contactar o no a un paciente antes una cita médica programada. 

Este sistema debe basarse en una serie de reglas de negocio definidas por cada institución de salud, las cuales pueden variar significativamente y modificarse con el tiempo. 

El componente "filtrar citas" debe tomar una conjunto de citas y una lista de reglas como entrada, y producir un subconjunto de las citas iniciales que cumplan con al menos una regla activa que indique la necesidad de contacto con el paciente en el día en curso. 

Este módulo fue diseñado con la capacidad de adaptar el sistema a nuevas reglas y modificaciones sin necesidad de alterar el código principal.

[Link al ejercicio técnico original](/https://ceroai.notion.site/Ejercicio-Filtros-de-citas-1f12afc1c42d80bb8a04f013a5f050ed#1f12afc1c42d806a87cfd1dd7f380083)

## Documentación Adicional

- [Diseño de MVE y Supuestos](/)
- [Exclusiones](/)
- [Valor que Aporta la Solución](/)
- [Parte 3 - Algunas preguntas](/)

## Pre-requisitos
- Python 3.11+
  
## Configuración Inicial 🛠️

### Paso 1: Clona el repositorio
```
git clone https://github.com/manjurulhoque/doccure.git
```

### Paso 2: Crea un ambiente virtual
```
py -m venv venv
venv\Scripts\activate source 
```

### Paso 3: Instala las dependencias
```
pip install -r requirements.txt
```

### Paso 4: Crea el archivo citas.json (input del módulo)
Este archivo se genera en base a un [archivo de google sheets](/https://docs.google.com/spreadsheets/d/1-4MUM3TyGO5rbDo-2fgphXoW_vvNZk96oqJJeMRglmI/edit?usp=sharing)

```
py src/consultar_citas.py
```

### Paso 5: Ejecuta el módulo filtrar_citas 

```
py src/filtrar_citas.py
```

Hecho con ❤️ y un par de 🐈‍⬛🐈‍⬛

<!-- 
### Parameters and Configuration
Environment Variables:
| Environment variable name | Description | Example |
| --- | --- | --- |
| GOOGLE_APPLICATION_CREDENTIALS | This variable represent the local path where the service account token was created previously. | /path/service/account/
| PROJECT_ID | This variable represent the project Id in Google Cloud where this service are going to be runned. | projectId


eg:
```json
{
  "country": "cl",
  "entity": "products",
  "endpoint": "https://api.us-central1.gcp.commercetools.com/adelco-dev/products",
  "output_bucket": "sandbox",
  "output_table": "CT.products",
  "date": "2023/08/25/08",
}
``` -->

<!-- ## Request

`POST /get_ct_products/`

```sh
curl --location 'http://localhost:9666/get_ct_products' \
--header 'Content-Type: application/json' \
--data '{"country":"cl", "entity": "products", "endpoint": "https://api.us-central1.gcp.commercetools.com/adelco-dev/products", "output_bucket": "sandbox", "output_table": "CT.products"}'
```

 -->