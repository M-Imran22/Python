import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
my_api_key = os.getenv("GOOGLE_GEMINI_API")
genai.configure(api_key=my_api_key)

model = genai.GenerativeModel('gemini-2.0-flash')

user_response = ""
while user_response.lower() != "exit":
    try:
        user_response = input(
            "Enter your prompt please.(type 'exit' to quit.)\n")
        if user_response.lower() != "exit":
            response = model.generate_content(user_response)
            print("\nResponse:\n")
            print(response.text)
            print("\n" + "-"*50 + "\n")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please try again.\n")
