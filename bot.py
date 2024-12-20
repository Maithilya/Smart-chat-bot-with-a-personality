import os
from config2 import apikey
os.environ["GOOGLE_API_KEY"] = apikey
import google.generativeai as genai

genai.configure(api_key=os.getenv(apikey))

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config= generation_config,
  #you can change the sysytem instruction according to the personality you want in this chat bot 
  system_instruction="your name is chottu and i am your maalk you have to be humorous and give specfic answes to me, rember that i m a big fan of bollywood movies so you can add refrences of this movies in our conversation but keep it short and sweet",
)


history=[]
print("Bot: Hello,how can I help you?")
while True:
  user_input = input("You: ")
  chat_session = model.start_chat(
    history=history
  )
  response=chat_session.send_message(user_input)
  model_response=response.text
  print(f'Bot: {model_response}')
  history.append({"role":"user","parts": [user_input]})
  history.append({"role":"model","parts": [model_response]})
