import os
import requests

def generate_code_from_hf(prompt: str, max_length: int = 200) -> str:
    """
    Generate code using the Hugging Face Inference API.

    Parameters:
      prompt (str): The code prompt or instruction.
      max_length (int): Maximum number of tokens to generate.

    Returns:
      str: The generated code or an error message.
    """
    API_URL = "https://api-inference.huggingface.co/models/deepseek-ai/deepseek-coder-6.7b"
    hf_token = os.environ.get("HF_TOKEN")
    if not hf_token:
        return "Error: HF_TOKEN environment variable not set."

    headers = {"Authorization": f"Bearer {hf_token}"}
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": max_length}
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code != 200:
        return f"Error: {response.status_code}, {response.text}"
    try:
        output = response.json()
        # Expected output is a list of dicts containing "generated_text"
        if isinstance(output, list) and output and "generated_text" in output[0]:
            return output[0]["generated_text"]
        return str(output)
    except Exception as e:
        return f"Error parsing response: {e}"
