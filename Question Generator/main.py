import tkinter as tk
from tkinter import messagebox
from nlp import QuestionGenerator

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Preguntas Automáticas")
        self.root.geometry("600x500")
        
        # Instanciamos el generador de preguntas
        self.generator = QuestionGenerator()

        # Interfaz gráfica
        self.setup_ui()

    def setup_ui(self):
        # Etiqueta de instrucciones
        self.instruction_label = tk.Label(self.root, text="Introduce un texto largo para generar preguntas", font=("Helvetica", 14))
        self.instruction_label.pack(pady=20)

        # Campo de entrada de texto
        self.text_entry = tk.Text(self.root, height=10, width=60)
        self.text_entry.pack(pady=10)

        # Botón para generar preguntas
        self.generate_button = tk.Button(self.root, text="Generar Preguntas", command=self.generate_questions, font=("Helvetica", 12))
        self.generate_button.pack(pady=10)

        # Etiqueta de preguntas generadas
        self.questions_label = tk.Label(self.root, text="Las preguntas generadas aparecerán aquí", font=("Helvetica", 12), wraplength=500)
        self.questions_label.pack(pady=20)

    def generate_questions(self):
        # Obtener el texto del campo de entrada
        text = self.text_entry.get("1.0", "end-1c").strip()
        
        if not text:
            messagebox.showwarning("Advertencia", "Por favor, introduce un texto.")
            return
        
        # Generar preguntas utilizando el generador NLP
        questions = self.generator.generate_questions(text, num_questions=3)
        
        if not questions:
            messagebox.showwarning("Advertencia", "No se generaron preguntas. Intenta con otro texto.")
            return
        
        # Mostrar las preguntas generadas
        questions_text = "\n".join([f"{i+1}. {q}" for i, q in enumerate(questions)])
        self.questions_label.config(text=f"Preguntas generadas:\n{questions_text}")

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
