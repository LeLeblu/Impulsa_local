import os
import google.generativeai as genai

# Configuramos la clave que ya guardaste en tu sistema
genai.configure(api_key="AIzaSyB1A9IAgLXJ63gQL2IbVVw6mrLT8bIKWv4")
model = genai.GenerativeModel('gemini-1.5-flash') # O 'gemini-pro'

# Iniciamos una sesión de chat con historial vacío
chat = model.start_chat(history=[])

print("--- Chat de Gemini Iniciado (Escribe 'salir' para terminar) ---")

while True:
    user_input = input("Tú: ")
    
    if user_input.lower() in ["salir", "exit", "quit"]:
        print("¡Adiós!")
        break
    # Enviamos el mensaje y recibimos la respuesta
    response = chat.send_message(user_input)
    
    print(f"\nGemini: {response.text}\n")