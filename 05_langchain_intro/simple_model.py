import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

# Load environment variables (API key)
os.environ["GOOGLE_API_KEY"] = "YOUR_GOOGLE_API_KEY"

# Initialize the Gemini chat model
chat = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.1
)

# Define the system role and user message
messages = [
    SystemMessage(
        content="تو یک معلم زبان آلمانی هستی. پاسخ دانش‌آموز رو به‌صورت خلاصه و با یک مثال کوتاه رایج و عامیانه بده."
    ),
    HumanMessage(
        content="ترجمه‌ی کلمه‌ی «دانشگاه» به آلمانی چی میشه؟"
    )
]

# Send the request and get the response
response = chat.invoke(messages)

# Print the text response of the model
print("--- Model Response ---")
print(response.content)

# Print metadata and token usage statistics
print("\n--- Token Usage Statistics ---")
print(f"Input: {response.usage_metadata['input_tokens']}")
print(f"Output: {response.usage_metadata['output_tokens']}")
print(f"Total: {response.usage_metadata['total_tokens']}")
