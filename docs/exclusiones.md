
## Exclusiones 🙅🏻 y Consideraciones para Próximos Pasos 👣 

Para mantener la simplicidad de esta primera versión se excluyen los siguientes casos borde:

- Si una cita se es ingresada el mismo día que se ejecuta el proceso, si esta no cumple con ninguna de las reglas activas el paciente no será contactado.

- Se considera que el proceso se ejecuta de manera diaria en la madrugada del día en curso, pero dependiendo del contexto de la institución (Ej. si se agendan muchas citas dentro del mismo día) podría ejecutarse el proceso nuevamente sólo para aquellas citas ingresadas posterior a la ejecución anterior del proceso.

- Si una cita cambia de estado (Ej. pasa de "agendada" a "confirmada"/"cancelada" a través de otro flujo) entre que se ejecuto el proceso de filtrado y el contacto con el paciente este si será contactado. Para futuras versiones se podría considerar un módulo de validación previo al contacto que permita excluir al cliente de ser contactado si así se desea.
  
- Si un paciente tiene más de una cita agendada para el mismo día este será contactado para cada una de ellas, en futuras versiones podría agregarse un módulo posterior al de filtrado de citas que permita identificar si un paciente tiene más de una cita y crear un flujo alternativo de contactabilidad que incluya la información de todas las citas en un mismo contacto.


