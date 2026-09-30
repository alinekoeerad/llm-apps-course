import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from the .env file
load_dotenv()

# Initialize the model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.1
)

message = "ترجمه‌ی کلمه‌ی «دانشگاه» به آلمانی چی میشه؟"
response = model.invoke(message)
print(response.content)
