import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
my_api_key = os.getenv("GOOGLE_GEMINI_API")
genai.configure(api_key=my_api_key)

model = genai.GenerativeModel('gemini-2.0-flash')

response = model.generate_content("Explain how AI works in simple terms")

print(response.text)
