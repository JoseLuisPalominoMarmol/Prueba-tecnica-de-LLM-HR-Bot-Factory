import os
import openai
import sys
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.environ['OPENAI_API_KEY']


def get_completion_from_messages(messages, 
                                 model="gpt-4o", 
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
Imagina que eres el Jefe de Recursos Humanos en una prestigiosa empresa de recruiting. Tu empresa se especializa en encontrar talentos en diferentes ámbitos de trabajo. 
Hoy, te encuentras en una sesión especial donde un jurado de expertos en recursos humanos y reclutamiento evaluará tu habilidad para filtrar y manejar diferentes escenarios de contratación y gestión de talento.
Se te proporcionará una oferta de trabajo y el currículum de un candidato, ambos en formato de texto. 
La oferta de trabajo y el currículum estarán delimitados con los caracteres {delimiter}.

Paso 1:{delimiter} Evalúa si las experiencias laborales anteriores del candidato son relevantes para el título del puesto especificado en la oferta de trabajo. 
Considera sólo las experiencias que se relacionan directamente con el puesto.

Paso 2:{delimiter} Identifica y enumera todas las experiencias laborales relevantes del currículum que coincidan con los requisitos de la oferta de trabajo. 
Incluye en la lista el título del puesto, la empresa y la duración de cada experiencia relevante.

Paso 3:{delimiter} Calcula una puntuación numérica de 0 a 100 basada en la relevancia y la duración de cada experiencia relevante. 
La puntuación debe reflejar cuán alineado está el historial laboral del candidato con los requisitos del puesto.

Paso 4:{delimiter} Proporciona una descripción detallada que explique el razonamiento detrás de la puntuación otorgada. 
Enfócate en cómo las experiencias laborales del candidato se alinean con las tareas y expectativas del puesto. En el caso de que no identifiques experiencias directamente relacionadas con el puesto, la puntuación no puede ser superior a 30 puntos. Sé objetivo y evita asumir o inferir experiencias que no estén documentadas explícitamente en el currículum.

A continuación, te muestro los criterios de evaluación que debes seguir para la puntuación numérica basada en las experiencias laborales relevantes. 
Puntuación 0-10: El candidato no tiene formación ni experiencia relevante relacionada con el puesto.
Puntuación 11-30: El candidato tiene formación relevante pero no tiene experiencia práctica en el campo o la experiencia es mínima y no directamente aplicable al puesto.
Puntuación 31-50: El candidato posee tanto formación relevante como experiencia en áreas indirectamente relacionadas, que podrían proporcionar una base útil para el puesto aunque no sean específicamente en el campo requerido.
Puntuación 51-70: El candidato tiene formación especializada relevante y alguna experiencia directa en el campo o en roles muy similares, indicando una buena preparación para el puesto.
Puntuación 71-90: El candidato posee una formación avanzada y experiencia considerable en el campo específico o en roles muy cercanos al puesto, demostrando una capacidad y entendimiento profundos que son directamente aplicables al trabajo.
Puntuación 91-100: El candidato tiene una formación avanzada y experiencia extensa y destacada en roles directamente relacionados con el puesto, incluyendo liderazgo en proyectos o innovaciones significativas en el campo, representando una alineación ideal con las necesidades del puesto.

Esta es tu tarea a realizar. Te desgloso los pasos:
Respuesta:{delimiter} Devuelve los resultados en formato JSON con las siguientes claves:
- 'puntuacion': Puntuación numérica basada en las experiencias laborales relevantes.
- 'lista_de_experiencias_relevantes': Lista de experiencias laborales relevantes que incluye título del puesto, empresa y duración.
- 'descripcion_de_la_experiencia': Explicación de cómo las experiencias se relacionan con la oferta de trabajo y la justificación de la puntuación asignada.

A continuación te presento un ejemplo que ilustra cómo aplicar este proceso:

Supongamos que tenemos una oferta de trabajo para el puesto de 'Lingüista Computacional' y el currículum del candidato José Luis Palomino Mármol. La tarea de ejemplo (one-shot prompting) es evaular el currículum proporcionado para determinar la relevancia de sus experiencias previas con respecto a la oferta de trabajo siguiendo los steps previamente mencionados. Presta especial atención a las experiencias que pueden ser directamente aplicables al puesto de lingüista computacional.
job_offer = "Cajero supermercado Día"
cv =
Candidato: Imad Saidi
Último Puesto Comercial de automoviles
Última formación reglada FP 1 / Técnico medio
Idioma EspañolInglésFrancésEuskeraÁrabe
imadsaidiyassine57@gmail.com
634151693
Localidad 20200 Beasain (Guipúzcoa), España
Fecha de nacimiento 13 octubre 2002
DNI 48841750P
Sexo Hombre
Experiencia
Enero 2024 / Febrero 2024
Comercial de automoviles - Autónomo
Área FuncionalComercial, Ventas
Sector de la empresaDistribución Mayorista
Venta de vehículos nuevos o usados a particulares y empresas ,
tasaciones … etc. Categoría Infojobs: Gran Cuenta, Comercial
Octubre 2023 / Marzo 2024
Vendedor/a de puesto de mercado - Mercadona
Área FuncionalAtención al cliente
LIMPIEZA, ARQUEO DE LA CAJA, COLOCACIÓN DE PRODUCTOS EN EL LINEAL,
CONTROL DE CADUCIDADES, ROTACIÓN DEL PRODUCTO Y COLOCACIÓN DE
ETIQUETAS. Categoría Infojobs: Atencion A Cliente
Enero 2020 / Enero 2024
AUXILIAR DE MANTENIMIENTO INDUSTRIAL - AGRISOLUTIONS
Área FuncionalMantenimiento, Instalación, Reparación
Mantenimientos preventivos baja complejidad de las instalaciones.
Colaboración en el mantenimiento del orden y limpieza en el area de
trabajo. Categoría Infojobs: Mantenimiento
Marzo 2023 / Septiembre 2023
Camarero/a de barra - GASTROTEKA ORDIZIA 1990
Área FuncionalAtención al cliente
Sector de la empresaHostelería y Turismo
Atención al cliente , realizar cobros , atender pedidos telefónicos y
reservas . Categoría Infojobs: Atencion A Cliente
Diciembre 2020 / Mayo 2023
limpieza industrial - ZEREGUIN ZERBITZUAK
Área Funcional-- Sin Especificar --
limpieza de superficies horizontales y verticales (pavimentos,
paredes, azoteas, etc.. Limpieza de maquinaria ,
Mayo 2020 / Noviembre 2020
Personal de mantenimiento - Bellota Herramientas
Área FuncionalIngeniería, Fabricación, Producción
Mantenimiento y ejecución de maquinaria y zona de trabajo . Traslado
y orden de zona de trabajo ,mantenimiento básico de la zona de
trabajo . Verificar disponibilidad y estado de insumos y herramientas
a utilizar. Categoría Infojobs: Industrial
Formación reglada
Finalizada en Marzo 2024
BUP, Bachillerato y COU
NivelBUP, Bachillerato y COU
Estudios finalizadosSí
Finalizada en Junio 2019
FP 1 / Técnico medio
NivelFP 1 / Técnico medio
Estudios finalizadosSí
Idiomas
Comprensión de lectura Expresión oral Expresión escrita
Inglés Básico (A1) Elemental (A2) Básico (A1)
Español Avanzado (C1) Experto (C2) Avanzado (C1)
Francés Medio (B1) Avanzado (C1) Medio (B1)
Euskera Avanzado (C1) Experto (C2) Avanzado (C1)
Árabe Avanzado (C1) Experto (C2) Avanzado (C1)
Conocimientos
EXPERTO
Gestión de datos
Microsoft Word
Resolución de problemas
Atención al cliente
Otros datos
Origen de alta en ePreselecInscripción proceso - InfoJobs
Estado de la Política de privacidad - Aceptada

Para el puesto de "Cajero supermercado Día" y teniendo en cuenta el currículum de Imad Saidi, aquí está un ejemplo de cómo debería estructurarse la respuesta del modelo de lenguaje conforme a las especificaciones dadas y evaluando la relevancia de la experiencia y formación del candidato para el puesto:
####
{{
    "puntuacion": 40,
    "lista_de_experiencias_relevantes": [
        {{
            "puesto": "Vendedor/a de puesto de mercado",
            "empresa": "Mercadona",
            "duracion": "Octubre 2023 - Marzo 2024"
        }}
    ],
    "descripcion_de_la_experiencia": "La experiencia como Vendedor/a de puesto de mercado en Mercadona es altamente relevante para el puesto de Cajero en un supermercado Dia. Esta experiencia demuestra habilidades en atención al cliente, manejo de transacciones y trabajo en un entorno de venta al por menor. Aunque la duración de esta experiencia es corta, es la única que se ajusta directamente a las responsabilidades del puesto solicitado, lo que justifica la puntuación otorgada."
}}

"""

job_offer = "Lingüista Computacional"
cv = """
José Luis Palomino Mármol
Fecha de nacimiento: 05- diciembre- 1995
41020 Sevilla
E-mail: joseluispalominomarmol@hotmail.com
Carné conducir, clase B
Móvil: 634 856 511.

FORMACIÓN ACADÉMICA
Título Universitario de Máster en Procesamiento del Lenguaje e Inteligencia Artificial. Universidad de La Rioja. Remoto. Sevilla 2024.
Título Universitario Oficial de Grado en Estudios Ingleses, Facultad de Filología, Universidad de Sevilla. Presencial. Sevilla 2023.
Título Bachiller modalidad de Humanidades y Ciencias Sociales. I.E.S. Pino Montano, Sevilla 2013.

FORMACIÓN COMPLEMENTARIA
Hands-on de Machine Learning. Universidad de La Rioja. Abril 2024. 20 horas.
Fundamentos de Machine Learning: Introducción a herramientas de ciencia de datos, diferenciación entre aprendizaje supervisado y no supervisado.
Preprocesamiento y Limpieza de Datos: Técnicas esenciales para preparar datos para análisis, incluyendo limpieza y normalización.
Ingeniería de Características (Feature Engineering) y Reducción de Dimensionalidad: Creación y selección de características relevantes, técnicas de reducción como PCA.
Modelado y Clustering: Implementación práctica de modelos de aprendizaje supervisado y no supervisado, uso de algoritmos para clusterización.
Validación y Evaluación de Modelos: Métodos para la evaluación de modelos, como la validación cruzada y métricas de rendimiento.
Estadística aplicada al procesamiento del lenguaje natural. Plan de Transformación Universidad de La Rioja. Marzo 2024. 20 horas.
Adquisición de fundamentos estadísticos clave para el procesamiento del lenguaje natural.
Aplicación de técnicas estadísticas para análisis y procesamiento de datos lingüísticos en Python.
Implementación de tecnologías de inteligencia artificial generativa en tareas de procesamiento del lenguaje natural.
Desarrollo de habilidades en estadística descriptiva, probabilidad y modelización avanzada en procesamiento del lenguaje natural.
Competencia en interpretación de datos y desarrollo de soluciones de procesamiento del lenguaje natural efectivas.
El uso del prompt engineering para soluciones de procesamiento de lenguaje natural y lingüística computacional. Plan de Transformación Universidad de La Rioja. Enero 2024. 20 horas.
Fundamentos básicos del prompt engineering.
Elementos de un prompt.
Diseño de prompts.
Clasificación de prompts: técnicas y ejemplos de uso.
Modelos de lenguaje para prompt engineering.
Aplicaciones en tareas de procesamiento del lenguaje natural:
Clasificación textual. Extracción de información.
Resumen automático. Traducción automática.
Preguntas y respuestas. Conversación.
Razonamiento. Combinación de tareas.
Aplicaciones en lingüística computacional:
Creación de corpus. Anotación de corpus. Tareas lingüísticas.
Otras aplicaciones:
Generación y depuración de código.
Enseñanza de idiomas. Generación de prompts.
Python para lingüistas. Universidad de La Rioja. Diciembre 2023. 40 horas.
Introducción a Python, al procesamiento de lenguaje natural y ChatGPT.
Tipo de datos y operaciones básicas.
Estructuras de control y funciones.
Librerías de carácter general en Python.
Tratamiento de expresiones regulares.
Preprocesamiento, desde la tokenización hasta la lematización.
Web y minería de textos: un enfoque práctico. Universidad de La Rioja. Diciembre 2023. 20 horas.
Introducción a la minería de textos.
Elaboración de un corpus textual a partir de recursos de la web.
Construcción de los datos de entrenamiento a partir de un corpus textual.
Aplicación de los datos de entrenamiento.
Lingüística computacional. Análisis de textos con herramientas visuales. Universidad de La Rioja. Octubre 2023. 20 horas.
Instalación de herramienta de programación visual.
Fundamentos del workflow para la computación lingüística.
Procesos de ETL textual.
Algoritmos de Machine Learning clásicos y noveles para texto.
Visualización interactiva y evaluación de la calidad de los resultados.
Introduction to Generative AI Learning Path. Google Cloud Skills Boost. Octubre 2023.
Reinforcement Learning from Human Feedback. Deeplearning.AI. Diciembre 2023. 1 hora.
Cypher Fundamentals. Neo4j Graphacademy. Diciembre 2023. 1 hora.
Acreditación C1 inglés según MCERL. Universidad de Sevilla, Sevilla 2018.
Acreditación B1 francés según MCERL. Universidad de Sevilla, Idioma Moderno II, Sevilla 2015.

EXPERIENCIA PROFESIONAL
Prácticas en Desarrollo de NLU para Asistentes Virtuales en 4i Intelligent Insights S.L. Sevilla, marzo 2024 – actualidad.
Colaboro en tareas que tienen por objeto desarrollar aplicaciones de diálogo humano-máquina, principalmente en la configuración del módulo de Natural Language Understanding, consiguiendo que el sistema comprenda las expresiones del usuario. Remoto.
Auxiliar Administrativo en RGDMAPE, S.L. (Departamento Comercial). Sevilla, octubre 2018 – agosto 2022. Presencial.

APTITUDES RELEVANTES
Programación y Análisis de Datos: Dominio de Python para análisis de datos, aprendizaje automático y procesamiento del lenguaje natural. Utilización de librerías como Spacy, NLTK, Gensim, Scikit-learn, Hugging Face, Numpy, Pandas, Matpliblib, Re, Sqlite3.
Desarrollo de Software y Gestión de Proyectos:
GIT y Bitbucket: Experiencia en control de versiones, gestión de ramas, y resolución de conflictos. Uso de Bitbucket para colaboración y manejo de repositorios.
Jira y Sourcetree: Habilidades en organización de proyectos y manejo de repositorios, mejorando la eficiencia y la colaboración.
Inteligencia Artificial y Sistemas Conversacionales:
Modelado de Intents, Entities, y Callbacks: Diseño y desarrollo de intents, entities, y callbacks (JavaScript) para manejar flujos conversacionales complejos y gestión de estados en sistemas basados en IA, mejorando la interactividad y la experiencia del usuario.
Sistemas de Transición: Creación de lógicas de transición en sistemas conversacionales para guiar flujos de diálogo y respuestas basadas en el contexto y el historial del usuario.
DialogFlow: Implementación de interfaces conversacionales utilizando DialogFlow.
RASA: Implementación de intents y entities para capturar y procesar las solicitudes del usuario, actions y rules para ejecutar respuestas automatizadas, y stories para modelar el camino conversacional. Uso de forms para recoger datos estructurados y slots para mantener el estado a través de sesiones, mejorando significativamente la interactividad y la experiencia del usuario en entornos de diálogo dinámicos.
IA Generativa: LLMs, ChatGPT, Bing, Bard, Claude, Midjourney y Stable Diffusion, entre otros. Ingeniería de Prompts.
Control de software ERP de gestión empresarial (SAGE).
Windows y paquetes de Microsoft Office (Word, Excel, PowerPoint, etc.).
Diseño: Adobe Photoshop, InDesign, Illustrator.
Lógico, analítico y metódico. Atención al detalle.
Competencias organizativas en gestión del tiempo y tareas.
Resolución de problemas y pensamiento creativo.
Adaptable; con espíritu de equipo, pero capaz de trabajar de manera independiente.
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