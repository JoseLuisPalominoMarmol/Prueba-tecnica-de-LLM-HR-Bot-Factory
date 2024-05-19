import os
import openai
import sys
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.environ['OPENAI_API_KEY']


def get_completion_from_messages(messages, 
                                 model="gpt-3.5-turbo", 
                                 temperature=0, max_tokens=500):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens, 
    )
    return response.choices[0].message["content"]


delimiter = "####"
system_message = f"""
Se te proporcionará una oferta de trabajo y el currículum de un candidato, ambos en formato de texto. \
La oferta de trabajo y el currículum estarán delimitados con los caracteres {delimiter}.

Paso 1:{delimiter} Evalúa si las experiencias laborales anteriores del candidato son relevantes para el título del puesto especificado en la oferta de trabajo. \
Considera sólo las experiencias que se relacionan directamente con el puesto.

Paso 2:{delimiter} Identifica y enumera todas las experiencias laborales relevantes del currículum que coincidan con los requisitos de la oferta de trabajo. \
Incluye en la lista el título del puesto, la empresa y la duración de cada experiencia relevante.

Paso 3:{delimiter} Calcula una puntuación numérica de 0 a 100 basada en la relevancia y la duración de cada experiencia relevante. \
La puntuación debe reflejar cuán alineado está el historial laboral del candidato con los requisitos del puesto.

Paso 4:{delimiter} Proporciona una descripción detallada que explique el razonamiento detrás de la puntuación otorgada. \
Enfócate en cómo las experiencias laborales del candidato se alinean con las tareas y expectativas del puesto.

Respuesta:{delimiter} Devuelve los resultados en formato JSON con las siguientes claves:
- 'puntuacion': Puntuación numérica basada en las experiencias laborales relevantes.
- 'lista_de_experiencias_relevantes': Lista de experiencias laborales relevantes que incluye título del puesto, empresa y duración.
- 'descripcion_de_la_experiencia': Explicación de cómo las experiencias se relacionan con la oferta de trabajo y la justificación de la puntuación asignada.
"""

job_offer = "Cajero supermercado Dia"
cv = """
Candidato: Imad Saidi
Último Puesto: Comercial de automóviles
Última formación reglada: FP 1 / Técnico medio
Idiomas: Español, Inglés, Francés, Euskera, Árabe
Correo electrónico: imadsaidiyassine57@gmail.com
Localidad: 20200 Beasain (Guipúzcoa), España
Fecha de nacimiento: 13 de octubre de 2002
DNI: 48841750P
Sexo: Hombre
Experiencia:
  - Enero 2024 / Febrero 2024: Comercial de automóviles - Autónomo
  - Octubre 2023 / Marzo 2024: Vendedor/a de puesto de mercado - Mercadona
  - Marzo 2023 / Septiembre 2023: Camarero/a de barra - GASTROTEKA ORDIZIA 1990
  - Diciembre 2020 / Mayo 2023: Limpieza industrial - ZEREGUIN ZERBITZUAK
  - Mayo 2020 / Noviembre 2020: Personal de mantenimiento - Bellota Herramientas
Formación reglada:
  - Marzo 2024: BUP, Bachillerato y COU
  - Junio 2019: FP 1 / Técnico medio
Idiomas:
  - Inglés: Básico (A1), Elemental (A2)
  - Español: Avanzado (C1), Experto (C2)
  - Francés: Medio (B1), Avanzado (C1)
  - Euskera: Avanzado (C1), Experto (C2)
  - Árabe: Avanzado (C1), Experto (C2)
Conocimientos:
  - Gestión de datos
  - Microsoft Word
  - Resolución de problemas
  - Atención al cliente
"""

user_message = f"""
Por favor, evalúa la relevancia del currículum proporcionado para la oferta de trabajo "{job_offer}", utilizando exclusivamente el curriculum proporcionado "{cv}". Considera los puestos, empresas y duraciones listadas en la sección de experiencia del currículum y calcula una puntuación que refleje cuán bien las experiencias del candidato coinciden con los requisitos del trabajo."""

messages =  [  
{'role':'system', 
 'content': system_message},    
{'role':'user', 
 'content': f"{delimiter}{user_message}{delimiter}"},  
] 

response = get_completion_from_messages(messages)
print(response)