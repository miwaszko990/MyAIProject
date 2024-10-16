import openai
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Initialize the OpenAI client with the API key from .env
api_key = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI client
client = openai.OpenAI(api_key=api_key)

def chat_gpt(prompt):
    try:
        # Create a chat completion using the latest API structure
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Use 'gpt-4' if you have access
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        # Return the generated response
        return response.choices[0].message.content.strip()

    except openai.AuthenticationError:
        print("Authentication failed. Please check your API key.")
    except openai.RateLimitError as e:
        print(f"OpenAI API request exceeded rate limit: {e}. Please try again later.")
    except openai.APIConnectionError as e:
        print(f"Failed to connect to OpenAI API: {e}. Please check your network and try again.")
    except openai.APIError as e:
        print(f"OpenAI API returned an API Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        response = chat_gpt(user_input)
        print("Bot:", response)
