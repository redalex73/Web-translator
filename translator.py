import requests
from bs4 import BeautifulSoup
from langdetect import detect
from googletrans import Translator

# Extrae texto limpio del contenido principal de una página de Wikipedia
def extract_text_from_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Buscar solo el contenido principal del artículo
        content_div = soup.find('div', {'id': 'mw-content-text'})
        if not content_div:
            return "No se encontró contenido principal en la página."

        # Obtener todos los párrafos
        paragraphs = content_div.find_all('p')
        text = '\n\n'.join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))

        return text
    except Exception as e:
        return f"Error al extraer texto: {e}"

# Detecta automáticamente el idioma del texto
def detect_language(text):
    try:
        return detect(text)
    except Exception as e:
        return f"Error al detectar el idioma: {e}"

# Traduce texto a un idioma objetivo usando googletrans
def translate_text(text, dest_lang='en'):
    try:
        translator = Translator()
        # Si el texto es muy largo, puede dividirlo en fragmentos
        max_length = 4500  # límite recomendado para evitar errores
        parts = [text[i:i+max_length] for i in range(0, len(text), max_length)]
        translated_parts = [translator.translate(part, dest=dest_lang).text for part in parts]
        return '\n\n'.join(translated_parts)
    except Exception as e:
        return f"Error al traducir: {e}"
