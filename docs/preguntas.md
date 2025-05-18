## Parte 3 - Algunas Preguntas❓

1. **Un centro médico te pide directamente con carácter urgente modificar sus políticas de contacto con pacientes de manera que entra en conflicto con tu implementación actual. ¿Cuál sería tu estrategia para abordar esta situación?**	
   
    Mi estrategia se enfocaría en una respuesta ágil y pragmática. Lo primero sería comprender la urgencia real y los plazos esperados para la implementación de esta modificación por parte del centro médico. Esta información es crucial para dimensionar el esfuerzo.

    Además, se debe evaluar en detalle de qué manera específica la nueva política entra en conflicto con la implementación existente. Esto implica identificar si la modificación requiere: ajustes a la lógica de filtrado con información ya disponible (¿es posible extender la funcionalidad actual incorporando un nuevo validador de matching y actualizando las reglas?), si se requieren datos que actualmente no están disponibles (como información demográfica adicional) se debe evaluar la viabilidad y el tiempo estimado de para una nueva integración para obtener esta información. 

    En estos casos, se consideraría la posibilidad de implementar un "fix" inicial que permita cumplir con la urgencia utilizando una fuente de datos alternativa o un método de obtención menos ideal pero funcional a corto plazo. Esta solución temporal debera coexistir con el desarrollo de una integración más robusta y optimizada a futuro. 

    Lo más importante, más allá de la solicitud puntual, buscaría comprender el problema real que impulsa esta modificación. ¿Es un cambio en un protocolo médico específico? ¿Una respuesta a la retroalimentación de los pacientes? Entender el contexto podría ayudar a ver si la solución propuesta es la más adecuada o si existen alternativas más eficientes o que aporten mayor valor a largo plazo.
   

2. **Necesitas comunicar ciertas restricciones técnicas a representantes institucionales sin formación tecnológica. ¿Qué métodos utilizarías para asegurar una comunicación efectiva?**

    Mi estrategia en este caso, se centraría en adaptar el mensaje al contexto de la audiencia. Inicialmente, buscaría comprender el nivel de conocimiento técnico de estos representantes y su involucramiento con el problema, diferenciando entre stakeholders de alto nivel o personal operativo no técnico. 

    Teniendo esto en consideración, el método principal sería la utilización de una presentación visual clara y concisa (apoyándome en slides, demos o un diagramas que ilustren el proceso). Con el fin de señalar específicamente dónde radica la restricción técnica, evitando la vocabulario técnico. Un punto clave sería explorar si estas restricciones son inherentemente limitantes o si existen alternativas o soluciones posibles. 

    En caso de haber opciones, presentar una propuesta clara de cómo se podrían resolver o, en su defecto, qué se puede entregar dentro de las limitaciones actuales, buscando un punto medio que funcione para ambas partes. Es fundamental que la comunicación finalize siempre en una propuesta de solución, evitando un simple "no se puede hacer".

    Además, para asegurar la comprensión, realizaría chequeos constantes preguntando directamente y reformulando los puntos clave, confirmando que el mensaje ha sido recibido y entendido correctamente por los representantes institucionales.

3. **Ante la llegada simultánea de varias peticiones de modificación procedentes de distintas instituciones, ¿qué criterios aplicarías para establecer prioridades y cómo comunicarías estas decisiones?**

    En este caso aplicaría una serie de criterios para establecer prioridades de manera objetiva y transparente. 

    En primer lugar, evaluaría la percepción del cliente sobre la solicitud, distinguiendo si se trata de la corrección de una funcionalidad defectuosa o de una mejora adicional a lo ya existente, priorizando las primeras.

    Luego, evaluaría la relevancia de la modificación para la operación del cliente, identificando el impacto que la no implementación inmediata tendría en su funcionamiento diario y si existen soluciones alternativas temporales, considerando el contexto de otras solicitudes en curso para el mismo cliente, evaluando la importancia relativa de la nueva petición y la proximidad de la entrega de otras funcionalidades, buscando posibles "quick wins". 

    El valor estratégico del cliente para Cero sería otro criterio importante, dando prioridad a aquellos clientes clave. 

    Finalmente, analizaría si algunas modificaciones pueden consolidarse en una única solución, priorizando aquellas que resuelvan múltiples necesidades al mismo tiempo.

    La comunicación de estas decisiones se basaría en la claridad y la transparencia en los plazos, evitando respuestas vagas y proporcionando actualizaciones regulares sobre el estado de cada solicitud. El foco sería que el mensaje transmitido deje clara la importancia que se le otorga, la evaluación responsable de su petición y el compromiso de entregar la mejor solución posible, aunque esto pueda requerir tiempo y una dedicación específica del equipo, explicando las posibles limitaciones de recursos o la necesidad de una planificación cuidadosa.

4. **Has identificado que una institución proporciona datos en formatos inconsistentes, provocando errores intermitentes en tu sistema de filtrado. ¿Qué proceso seguirías para identificar el origen del problema y desarrollar una solución adecuada?**

    En este caso, lo principal seria identificar la raíz del problema y desarrollar una solución adecuada. Lo primero sería rastrear el origen de los errores, investigando si la inconsistencia se introduce en el módulo de "consultar citas" o si ya existe en los datos proporcionados por el sistema de origen de la institución.

    Si la inconsistencia se origina en el módulo de "consultar citas", exploraría la implementación de una capa adicional de validación y transformación para asegurar un formato de salida uniforme y estandarizado. 

    Por otro lado, si el problema se encuentra en el sistema de origen, evaluaría la posibilidad de obtener la información desde una fuente alternativa dentro de la misma institución que garantice mayor consistencia, o en su defecto evaluar la viabilidad de solicitar modificaciones en el sistema de origen para estandarizar el formato de los datos, considerando la complejidad y los recursos necesarios para ello.

    En el caso de que no sea posible asegurar la consistencia desde el origen, implementaría una capa robusta de limpieza y normalización de datos como parte del proceso de ingesta previo al filtrado, considerarndo las diferentes variaciones de formato para diseñar reglas de transformación que abarquen la mayor cantidad de las inconsistencias posibles. Sin embargo, consideraría la posibilidad de que persistan casos atípicos que requieran un manejo especial o que impidan el procesamiento de ciertas citas sin información adicional. 

    En cualquiera de los casos, el objetivo sería minimizar los errores y asegurar la mayor cobertura posible en el procesamiento de las citas, documentando y transparentando al cliente cualquier limitación o posible pérdida de información debido a las inconsistencias en los datos de origen.