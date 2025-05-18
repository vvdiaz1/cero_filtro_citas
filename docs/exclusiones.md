
## Exclusiones 🙅🏻 y Consideraciones para Próximos Pasos 👣 

Para mantener la simplicidad de esta primera versión se excluyen los siguientes casos borde o condiciones del problema:

- Si una cita se es ingresada el mismo día que se ejecuta el proceso, si esta no cumple con ninguna de las reglas activas el paciente no será contactado.

- Se considera que el proceso se ejecuta de manera diaria en la madrugada del día en curso, pero dependiendo del contexto de la institución (Ej. si se agendan muchas citas dentro del mismo día). Una potencial mejora, podría se ejecutar el proceso nuevamente durante el día sólo para aquellas citas ingresadas posterior a la ejecución anterior del proceso.

- Si una cita cambia de estado (Ej. pasa de "agendada" a "confirmada"/"cancelada" a través de otro flujo) entre que se ejecutó el proceso de filtrado y el contacto con el paciente este si será contactado. Para futuras versiones se podría considerar un módulo de validación previo al contacto que permita excluir al cliente de ser contactado si así se desea.
  
- Si un paciente tiene más de una cita agendada para el mismo día este será contactado para cada una de ellas, en futuras versiones podría agregarse un módulo posterior al de filtrado de citas que permita identificar si un paciente tiene más de una cita por la cúal sera contactado durante el día y crear un flujo alternativo de contactabilidad que incluya la información de todas las citas en un mismo contacto con el paciente.

- En el diseño actual, en caso de que una cita cumpla con múltiples reglas, la decisión de contactar (o no contactar) se basa en la existencia de al menos una regla activa con la condición de enviar_mensaje en true. Si una regla con enviar_mensaje en false se cumple, de momento no prevalece la no contactabilidad. Para una futura versión se puede agregar esta lógica para evitar contactar a pacientes que deberian excluirse.

- En esta versión no se incluye la capacidad de filtrar a un conjunto de pacientes, para que sean excluidos de la contactabiliadad en cualquier caso, aún cuando califiquen según alguna regla (similar a la exclusión de un profesional), pero es posible incluirlo en una futura versión en la que exista una lista de exclusión (blacklist).

- Si bien se contruyó un pequeño módulo para replicar el comportamiento de consultar citas, este se excluye del detalle del prototipo ya que se utilizó sólo con fines de facilitar el desarrollo del módulo principal. Por lo que no está documentado de la misma forma que el resto del prototipo.