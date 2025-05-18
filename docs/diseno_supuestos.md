
## Diseño de MVE 🌟


## Supuestos 🤔

Para abordar este problema, se han realizado las siguientes suposiciones:

- **Formato Consistente de Citas:** Se asume que el módulo "consultar citas" entrega una lista de diccionarios con una estructura consistente dentro de cada institución, aunque pueda variar entre ellas, para este prototipo se considera sólo una institución. 

- **Calidad del Dato:** Se asume que el módulo consultar citas y/o integraciones a las API de la institución ya contienen ciertas reglas de validación para los télefonos de los pacientes y asegura que las citas consultadas son contactables. Sin embargo, el módulo de filtrado considera ciertas validaciones básicas de que el dato no venga vacio para los campos utilizados.

- **Campos Relevantes para Filtrado:** Se considera que las reglas de negocio pueden tener distintas utilizando la información ya contenida en la cita utilizando los campos: 

  - `profesional`: id, rut, nombre, apellido, especialidad
    - especialidad: contenido dentro de profesional, id, nombre
  - unidad medica: id, nombre es el lugar físico donde se realiza la cita
  - atención: id, tipo, lista, categoria
  - estado: id, nombre
  - paciente: id, nombre, apellido, rut, sexo, fecha nacimiento telefono
  - fecha y hora
  - 
   y hora, datos del paciente, etc.) estarán presentes, aunque sus nombres exactos puedan necesitar mapeo en un sistema real.

- **Contactabilidad por defecto:** En el caso de que alguna regla no contenga información sobre la cantidad de días previos a la cita en la cúal se debe contactar al paciente, se contactará el día previo a la cita

- **Ejecución Diaria:** Se asume que el proceso de filtrado se ejecuta diariamente (en la madrugada del día en curso) tomando como referencia la fecha actual para evaluar condiciones basadas en la proximidad de la cita.
<!-- - Prioridad de Reglas: En caso de que una cita cumpla con múltiples reglas, la decisión de contactar (o no contactar) se basa en la existencia de al menos una regla activa con la condición de enviar_mensaje en true. Si una regla con enviar_mensaje en false se cumple, prevalece la no contactabilidad. (Esta suposición puede refinarse si se requiere una lógica de prioridad más compleja entre reglas). -->

- **Atomicidad de las Condiciones:** Cada condición dentro de una regla se evalúa de forma independiente. Una regla se considera "cumplida" si todas las condiciones dentro de al menos uno de sus bloques de condiciones se satisfacen correctamente.

- **Flexibiliad para activar/modificar reglas:** El formato de input de las reglas cuenta con 3 campos que permite manejar la activación de estas (activa -> true/false) de manera de poder responder de forma rápida a solicitudes de los clientes, además cuenta con versionamiento (version) y fecha de modificación (fecha_modificacion) para poder tener un histórico de todas las reglas que se han ejecutado para cada institución. 
 
- **Simplicidad Inicial:** Para el MVE, el foco es implementar la lógica para las condiciones presentadas en las solicitudes de la Parte 2, dejando la estructura preparada para modificaciones dentro del universo de opciones presentado en el problema. Se podrían agregar más tipos de condiciones en iteraciones futuras, para asegurar un módulo más robusto.
  
- **Manejo de Fechas:** Todas las fechas trabajadas están en formato ISO (YYYY-MM-DD o YYYY-MM-DD HH:MM)
