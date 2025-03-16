# Code Copilot

Code Copilot is an AI-powered tool designed for **code correction, auto-completion, and debugging**. It leverages **Ollama** and the **DeepSeek Coder 6.7B** model to assist developers in writing high-quality code efficiently. The project features a **FastAPI backend** for handling LLM requests and a **Streamlit UI** for a user-friendly experience.

---

## 🚀 Features
- **Code Correction**: Fix syntax and logical errors in your code.
- **Auto-Completion**: Generate and complete code snippets based on prompts.
- **Debugging Assistance**: Identify and fix potential issues in your code.
- **FastAPI Backend**: Provides an API for interacting with the AI model.
- **Streamlit UI**: Simple and interactive user interface for developers.

---

## 📁 Project Structure
```
Code-Copilot/
│-- main.py         # FastAPI backend (LLM integration)
│-- app.py          # Streamlit UI
│-- test.py         # Local testing script
│-- requirements.txt # Project dependencies
│-- README.md       # Project documentation
```

---

## 🛠️ Installation & Setup
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/FAbdullah17/Code-Copilot.git
cd Code-Copilot
```

### 2️⃣ **Create a Virtual Environment** (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Run Ollama & Load DeepSeek Coder**
Make sure **Ollama** is installed and running:
```bash
ollama serve &
ollama pull deepseek-coder:6.7b
```

---

## 🚀 Running the Project
### **Start FastAPI Backend**
```bash
python main.py
```
- API will run at: **http://127.0.0.1:8000**
- Access API docs: **http://127.0.0.1:8000/docs**

### **Start Streamlit UI**
```bash
streamlit run app.py
```
- Open **http://localhost:8501** in your browser.

---

## 🧪 Testing
To test the API locally before deployment:
```bash
python test.py
```
Or use `cURL`:
```bash
curl -X 'POST' 'http://127.0.0.1:8000/generate' \
-H 'Content-Type: application/json' \
-d '{"prompt": "Write a Python function to add two numbers."}'
```

---

## 📜 API Endpoints
### **1. Root Endpoint**
- **GET** `/`
- Returns a status message.

### **2. Code Generation**
- **POST** `/generate`
- **Request Body:**
  ```json
  {
    "prompt": "Write a Python function to add two numbers."
  }
  ```
- **Response:**
  ```json
  {
    "response": "def add_numbers(a, b):\n    return a + b"
  }
  ```

---

## 🛠️ Technologies Used
- **Python** (FastAPI, Streamlit)
- **Ollama** (LLM Serving)
- **DeepSeek Coder 6.7B** (LLM Model)
- **Uvicorn** (FastAPI Server)

---

## 📌 Future Enhancements
- [ ] Improve model performance with fine-tuning.
- [ ] Add more debugging features.
- [ ] Deploy the project on cloud platforms.

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 🤝 Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a Pull Request

---

## 💬 Contact
For any inquiries or contributions, reach out via:
- **Email**: fahadai.co@gmail.com
- **GitHub**: [Fahad Abdullah](https://github.com/FAbdullah17)

Happy Coding! 🚀

