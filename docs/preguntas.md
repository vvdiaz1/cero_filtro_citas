## Parte 3 - Algunas Preguntas❓

1. **Un centro médico te pide directamente con carácter urgente modificar sus políticas de contacto con pacientes de manera que entra en conflicto con tu implementación actual. ¿Cuál sería tu estrategia para abordar esta situación?**	
   
   
   
- entender plazos esperados para la modificación (que es urgente)
- evaluar de que manera entra en conflicto con la implementación
    - falta agregar una variable por ejemplo hay que filtrar por sexo de la persona y no lo tengo contemplado en el flujo pero tengo la info y lo puedo agregar
    - la modificacion incluye informacion que no tengo y debo realizar una integracion nueva para tenerla, es esto suficientemente rapido o debo incorporar un fix inicial trayendo la info de una forma no idea pero que funciona que luego puedo optimizar (hacemos este tipo de cosas?)
- entender el problema mas que solo tomar el requrimiento (aplica aqui?) para ver si esta es la modificacion que hay que hacer o si es otra



1. **Necesitas comunicar ciertas restricciones técnicas a representantes institucionales sin formación tecnológica. ¿Qué métodos utilizarías para asegurar una comunicación efectiva?**
   
- primero que nada es importante entender el contexto del publico al que me dirijo, que conocimiento del problema tienen estos representantes institucionales son los stakeholders tipo directorio o es alguien no tecnico que esta en la operacion
- teniendo lo anterior en consideración hay que ver el mejor camino, idealmente tener una presentacion con slides tipo demo o algun diagrama que muestre el flujo y el punto donde esta el problema
- son estas restricciones tecnicas solucionables de alguna manera, de ser asi tenemos una propuesta de como resolverlas o alguna propuesta de que SI se puede entregar dado el problema actual (hay un punto medio que funcione para ambas partes?)
- siempre tiene que haber una propuesta final de solucion no puede cerrarse con NO se puede hacer
- hacer chequeo de la comprension, sobretodo con partes no tecnicas confirmar que entendieron de lo que estamos proponiendo o discutiendo (estamos hablando de lo mismo?)
- AGREGAR chequeo de gemini de si esta cumpliendo con la parte de metodos

3. **Ante la llegada simultánea de varias peticiones de modificación procedentes de distintas instituciones, ¿qué criterios aplicarías para establecer prioridades y cómo comunicarías estas decisiones?**

- cual es la percepcion del cliente sobre la solicitud, siente que es algo que esta fallando o es algo que quiere agregar a lo que ya tiene (es un nice to have o un must)
- que tan relevante es esta modificacion para la operacion del cliente, esto le genera algun problema en su operacion diaria que debera solucionar de otra forma hasta que este listo (cual es el impacto que tiene no tener esto para el cliente)
- es un cliente que ya tiene otras solicitudes en curso? es esta mas importante que las demas? algunas de las otras esta lista o se podra entregar pronto (podemos tener algun quick win con algo ademas de esto?
- cual es el valor del cliente para Cero, es un cliente importante o clave al que hay que darle atencion prioritaria
- algunas de las modificaciones se pueden “juntar” y resolver con solo una solucion, si es asi alguna de ellas esta mas arriba en la lista de prioridades segun los otros puntos

como comunicar

- siempre se claro con los plazos, no se puede ser vago en la respuesta, dar updates del estado de la modificacion para que sepa que se esta avanzando si es algo que toma mucho tiempo
- mensajes para el cliente: me importas, evalue esto con responsabilidad y llegue a esta conclusion; quiero entregarte la mejor solucion y bien hecha (eso puede necesitar tiempo del equipo o que pueda estar disponible full para esto y que eso no sea ahora)

4. **Has identificado que una institución proporciona datos en formatos inconsistentes, provocando errores intermitentes en tu sistema de filtrado. ¿Qué proceso seguirías para identificar el origen del problema y desarrollar una solución adecuada?**

- ir desde el punto en que se estan generando lo problemas hacia atras, es algo del modulo de consultar citas lo que genera la inconsistencia? o es el sistema de origen el que trae formatos inconsistentes
- si el problema es el modulo de consultar citas revisar como puedo agregar una capa adicional que asegure el formato de output fijo
- si es el sistema de origen, se puede sacar la información de algun otro lado donde pueda asegurar que esto no pasa? se puede modificar algo de ese sistema de manera “facil” para asegurar el formato?
- si no se puede hacer desde el sistema que envia los datos, agregar una capa de limpieza o normalizacion de los datos en mi ELT/ETL antes de proceder con el filtrado, tengo manera de captar todas las desviaciones de formato o quedaran citas que no puedo procesar sin agregar info adicional o modificando el origen de la ingesta