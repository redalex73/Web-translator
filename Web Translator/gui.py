import tkinter as tk
from tkinter import scrolledtext, messagebox
from tkinter import ttk
from translator import extract_text_from_url, detect_language, translate_text

class TranslatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Traductor de Páginas Web")

        # URL input
        self.url_label = tk.Label(root, text="Introduce la URL:")
        self.url_label.pack()

        self.url_entry = tk.Entry(root, width=80)
        self.url_entry.pack(pady=5)

        # Idioma de destino (Menú desplegable)
        self.lang_label = tk.Label(root, text="Selecciona el idioma de destino:")
        self.lang_label.pack()

        self.lang_options = ["en", "es", "fr", "de", "it", "pt", "ru", "zh-CN", "ja", "ar"]  # Lista de idiomas populares
        self.lang_combobox = ttk.Combobox(root, values=self.lang_options, width=10)
        self.lang_combobox.set("en")  # Idioma por defecto: inglés
        self.lang_combobox.pack(pady=5)

        # Botón de traducir
        self.translate_button = tk.Button(root, text="Traducir página", command=self.translate)
        self.translate_button.pack(pady=10)

        # Área de resultado
        self.output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=30)
        self.output_text.pack(pady=10)

    def translate(self):
        self.output_text.delete(1.0, tk.END)  # Limpiar campo
        url = self.url_entry.get()
        dest_lang = self.lang_combobox.get()  # Obtener el idioma seleccionado desde el menú

        if not url:
            messagebox.showerror("Error", "Por favor, introduce una URL.")
            return

        self.output_text.insert(tk.END, "Extrayendo texto de la página...\n")
        text = extract_text_from_url(url)

        if text.startswith("Error"):
            self.output_text.insert(tk.END, text)
            return

        self.output_text.insert(tk.END, f"Texto extraído correctamente.\nDetectando idioma...\n")

        lang = detect_language(text)
        self.output_text.insert(tk.END, f"Idioma detectado: {lang}\n")
        self.output_text.insert(tk.END, f"Traduciendo al {dest_lang}...\n\n")

        translated = translate_text(text, dest_lang)

        self.output_text.insert(tk.END, "--- TEXTO TRADUCIDO ---\n\n")
        self.output_text.insert(tk.END, translated)