import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Try to read the API keys
pplx_key = os.getenv('PPLX_API_KEY')
openai_key = os.getenv('API_KEY_OPENAI')

# Print the keys (but mask most of the characters for security)
def mask_key(key):
    return key[:4] + '*' * (len(key) - 8) + key[-4:] if key else None

print(f"PPLX API Key: {mask_key(pplx_key)}")
print(f"OpenAI API Key: {mask_key(openai_key)}")

# Check if keys are not None
if pplx_key and openai_key:
    print("Both API keys were successfully read from the .env file.")
else:
    print("Failed to read one or both API keys from the .env file.")