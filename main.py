from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import ollama

# Initialize FastAPI app
app = FastAPI()

# Define request model
class CodeRequest(BaseModel):
    prompt: str

# Root endpoint (optional, but prevents 404 error on "/")
@app.get("/")
async def root():
    return {"message": "Code Copilot API is running. Use /generate to send requests."}

# API endpoint for code generation
@app.post("/generate")
async def generate_code(request: CodeRequest):
    try:
        response = ollama.chat(model="deepseek-coder:6.7b", messages=[{"role": "user", "content": request.prompt}])
        return {"response": response["message"]["content"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run FastAPI when executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)