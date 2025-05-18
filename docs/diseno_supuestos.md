
# Diseño de MVE 🌟

El módulo "filtrar citas" se centra en un flujo de datos unidireccional donde las reglas de negocio y la información de las citas son las entradas (input), y la lista de citas filtradas (aquellas de los pacientes que deben ser contactados hoy) es la salida(output). 

El diseño contempla 3 etapas clave:
 - Carga de datos
 - Evaluación de reglas 
 - Filtrado de citas según reglas

![Diseño de MVE](/assets/imgs/MVE.png)

## Componentes Principales

### Carga de Datos

- **Cargador de Reglas:** Este componente es responsable de leer y parsear el archivo de reglas (reglas.json) que contiene las reglas de negocio definidas por la institución. La salida de este componente es una lista de diccionarios que representa las reglas.

- **Cargador de Citas:** Este componente toma la salida del módulo "consultar citas" (simulado en este MVE mediante la lectura del archivo citas.json). Su función es cargar y estructurar la información de las citas en una lista de diccionarios en memoria.

### Evaluación de reglas 

Este es el componente principal de la solución,recibe como entrada la lista de reglas cargadas y la lista de citas. Para cada cita, itera a través de las reglas activas y evalúa si la cita cumple con las condiciones especificadas para cada regla. Utiliza un conjunto de funciones de "matching" (como match_especialidad, match_profesional, match_dias_antes, etc.) para comparar los atributos de la cita con las condiciones de la regla y evaluar si la cumple.

- **Validadores de Matching:** Un conjunto de funciones de "matching" que consideran los campos relevantes para el filtrado de reglas, permitiendo así el dinamismo en las condiciones de estas, lo que habilita al diseño a incluir reglas más complejas en un futuro sin necesidad de modificar la estructura principal del sistema.
  
  - **Campos Relevantes para Filtrado:** Se considera que las reglas de negocio pueden tener distintas condiciones pero siempre utilizando la información ya contenida en la cita utilizando los siguientes campos: 

    - `profesional:` id, rut, nombre, apellido
    - `especialidad:` id, nombre (contenido dentro de profesional)
    - `unidad medica:` id, nombre (lugar físico donde se realiza la cita)
    - `atención:` id, tipo, lista
    - `estado:` id, nombre
    - `paciente:` id, rut, nombre, apellido, sexo, fecha de nacimiento
  
- **Evaluador de condiciones:** Componente que utiliza todos los Validadores de Matching para evaluar si una cita cumple con al menos una regla activa, utilizando las funciones anteriores. Si una cita "hace match" con una regla y enviar_mensaje es true, se incluye en la lista. Si una cita "hace match" con una regla activa donde enviar_mensaje es false, se excluye. Evaluando si la cita cumple o no con la/las condiciones para ser contactada. 


### Filtrado de citas según reglas  

- **Filtrado de citas**: Este componente entrega una lista de las citas que cumplen con los criterios para ser contactadas con el mismo formato en el que se ingresaron.Es decir, determina si el paciente de la cita debe ser contactado el día de hoy. 

## Supuestos 🤔

Para abordar este problema, se han realizado las siguientes suposiciones:

- **Formato Consistente de Citas:** Se asume que el módulo "consultar citas" entrega una lista de diccionarios con una estructura consistente dentro de cada institución, aunque pueda variar entre ellas, para este prototipo se considera sólo una institución. 

- **Calidad del Dato:** Se asume que el módulo consultar citas y/o integraciones a las API de la institución ya contienen ciertas reglas de validación para los télefonos de los pacientes y asegura que las citas consultadas son contactables. Sin embargo, el módulo de filtrado considera ciertas validaciones básicas de que el dato no venga vacio para los campos utilizados.

- **Contactabilidad por defecto:** En el caso de que alguna regla no contenga información sobre la cantidad de días previos a la cita en la cúal se debe contactar al paciente, se contactará el día previo a la cita

- **Ejecución Diaria:** Se asume que el proceso de filtrado se ejecuta diariamente (en la madrugada del día en curso) tomando como referencia la fecha actual para evaluar condiciones basadas en la proximidad de la cita.

- **Traslape de Reglas:** En caso de que una cita cumpla con múltiples reglas, la decisión de contactar (o no contactar) se basa en la existencia de al menos una regla activa con la condición de enviar_mensaje en true.

- **Atomicidad de las Condiciones:** Cada condición dentro de una regla se evalúa de forma independiente. Una regla se considera "cumplida" si todas las condiciones dentro de al menos uno de sus bloques de condiciones se satisfacen correctamente.

- **Flexibiliad para activar/modificar reglas:** El formato de input de las reglas cuenta con 3 campos que permite manejar la activación de estas (activa -> true/false) de manera de poder responder de forma rápida a solicitudes de los clientes, además cuenta con versionamiento (version) y fecha de modificación (fecha_modificacion) para poder tener un histórico de todas las reglas que se han ejecutado para cada institución. 

- **Requerimiento de id o Rut para Reglas:** Se asume que si bien en las reglas en algunos casos no se cuenta con el id o rut en caso de los profesionales y sólo su nombre o apellido, es necesario para la buena ejecución del proceso tener un identificador único para este. El sistema también permite la flexibilidad (en la mayor parte de los casos) de ingresar tanto el nombre como id para aquellos cambos que si lo permiten (Ej.estado, especialidad, etc)
 
- **Simplicidad Inicial:** Para el MVE, el foco es implementar la lógica para las condiciones presentadas en las solicitudes de la Parte 2, dejando la estructura preparada para modificaciones dentro del universo de opciones presentado en el problema. Se podrían agregar más tipos de condiciones en iteraciones futuras, para asegurar un módulo más robusto.
  
- **Manejo de Fechas:** Todas las fechas trabajadas están en formato ISO (YYYY-MM-DD o YYYY-MM-DD HH:MM)
