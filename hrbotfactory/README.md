# Prueba-tecnica-de-LLM-HR-Bot-Factory
Prueba técnica para optar al puesto de Prompt Engineer / LLM Expert en HR Bot Factory

hr bot factory
Prueba técnica de LLM - IA Gen

Descripción del proyecto
La prueba consta de diseñar un sistema basado en LLM y los Prompts necesarios para lograr
que una IA generativa (puede ser ChatGPT, Gemini, Claude, etc) te ayude a valorar la experiencia
de un candidato de una oferta de trabajo.

Especificaciones
Este sistema recibirá el nombre de una oferta de trabajo y un CV completo, ambos en formato
texto como strings) y debe tener una salida muy específica en formato JSON (diccionario) que
recogerá la puntuación obtenida, una lista de trabajos relacionados con el que queremos
evaluar y una descripción de porqué obtuvo la puntuación dada.

El sistema debe implementarse usando Python, conectando al API del modelo LLM elegido de
forma directa o usando la librería Langchain (como considere oportuno). El entregable debe ser
un proyecto instalable y 100% funcional.

Requisitos

1.Input: Adjuntamos al Prompt el CV de un candidato con todos sus datos y el título de
una oferta que describe el tipo de puesto que se está buscando, Ej: Cajero supermercado Dia.

2.Output: Todo el Output debe ser en formato JSON con la siguiente información:

a. Valor numérico con la puntuación de 0 a 100 según la experiencia: Se debe
tener en cuenta sólo los puestos de trabajo relacionados con el del título
aportado, por ejemplo no debe contar la experiencia como repartidor para un
puesto de cajero.

b. Listado de la experiencia: Debe devolver un listado con las experiencias que son
relacionadas a la oferta propuesta, este listado debe contener la siguiente
información de cada experiencia: Puesto, Empresa y duración.

c. Descripción de la experiencia: Debe devolver un texto explicativo sobre la
experiencia del candidato y porque ha obtenido la puntuación dada.

Spacy: 
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download es_core_news_sm