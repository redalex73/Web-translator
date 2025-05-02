from transformers import T5ForConditionalGeneration, T5Tokenizer

class QuestionGenerator:
    def __init__(self):
        # Cargar modelo y tokenizador preentrenado
        self.model = T5ForConditionalGeneration.from_pretrained("t5-small")
        self.tokenizer = T5Tokenizer.from_pretrained("t5-small")
    
    def generate_questions(self, text, num_questions=3):
        # Dividir el texto en fragmentos si es largo
        fragment_size = 300  # Tamaño máximo por fragmento
        fragments = [text[i:i+fragment_size] for i in range(0, len(text), fragment_size)]
        
        questions = []
        
        # Generar preguntas para cada fragmento
        for fragment in fragments:
            input_text = "generate questions: " + fragment
            input_ids = self.tokenizer.encode(input_text, return_tensors="pt")
            
            # Generar múltiples preguntas (ajustar la longitud según sea necesario)
            output = self.model.generate(input_ids, max_length=50, num_beams=4, num_return_sequences=num_questions, early_stopping=True)
            
            for seq in output:
                question = self.tokenizer.decode(seq, skip_special_tokens=True)
                questions.append(question)
        
        return questions
