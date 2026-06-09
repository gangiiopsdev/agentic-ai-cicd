from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string: str) -> bool:
    return input_string.isalnum() and len(input_string) <= 255

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not sanitize_input(host):
        return {"error": "Invalid input"}, 400
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {
        "status": "completed",
        "output": result.stdout,
        "stderr": result.stderr
    }