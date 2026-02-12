import os
from dotenv import load_dotenv
from google import genai

def main():
    # 1. Load environment variables
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    model_id = os.getenv("GOOGLE_MODEL", "gemini-2.0-flash-lite")

    if not api_key:
        print("Error: GOOGLE_API_KEY not found in .env file.")
        return

    # 2. Read prompt.md content
    prompt_path = "prompt.md"
    if not os.path.exists(prompt_path):
        print(f"Error: {prompt_path} not found.")
        return

    with open(prompt_path, "r", encoding="utf-8") as f:
        prompt_text = f.read()

    # 3. Initialize Gemini Client
    client = genai.Client(api_key=api_key)

    print(f"--- Calling Gemini Model: {model_id} ---")
    
    try:
        # 4. Generate content
        response = client.models.generate_content(
            model=model_id,
            contents=prompt_text
        )

        # 5. Print response
        print("\nResponse:")
        print(response.text)
        
    except Exception as e:
        print(f"An error occurred while calling the API: {e}")

if __name__ == "__main__":
    main()
