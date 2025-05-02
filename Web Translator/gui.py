import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from translator import extract_text_from_url, detect_language, translate_text

class TranslatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Traductor de Páginas Web")
        self.root.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Introduce la URL de la página web:", font=("Arial", 12)).pack(pady=10)
        
        self.url_entry = tk.Entry(self.root, width=80)
        self.url_entry.pack(pady=5)

        self.target_lang = tk.StringVar(value="es")
        lang_options = ["es", "en", "fr", "de", "it", "pt"]
        ttk.Label(self.root, text="Idioma de destino:").pack()
        ttk.Combobox(self.root, textvariable=self.target_lang, values=lang_options).pack(pady=5)

        self.translate_button = tk.Button(self.root, text="Traducir", command=self.translate_page)
        self.translate_button.pack(pady=10)

        self.output_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=100, height=25)
        self.output_area.pack(pady=10)

    def translate_page(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showwarning("Error", "Por favor introduce una URL.")
            return
        
        self.output_area.delete(1.0, tk.END)
        self.output_area.insert(tk.END, "Extrayendo texto de la página...\n")
        self.root.update()

        text = extract_text_from_url(url)
        if "Error" in text:
            self.output_area.insert(tk.END, text)
            return
        
        lang = detect_language(text)
        self.output_area.insert(tk.END, f"Idioma detectado: {lang}\nTraduciendo al {self.target_lang.get()}...\n")
        self.root.update()

        translated = translate_text(text, target_lang=self.target_lang.get())
        self.output_area.insert(tk.END, "\n--- TEXTO TRADUCIDO ---\n")
        self.output_area.insert(tk.END, translated)
