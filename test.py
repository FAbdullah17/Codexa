import ollama

# Function to test the LLM
def test_llm():
    prompt = input("Enter your prompt: ")
    response = ollama.chat(model="deepseek-coder:6.7b", messages=[{"role": "user", "content": prompt}])
    print("LLM Response:\n", response["message"]["content"])

# Run the test
if __name__ == "__main__":
    test_llm()