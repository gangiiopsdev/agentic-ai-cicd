from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True)

def sanitize_input(input_str: str) -> str:
    return ''.join(e for e in input_str if e.isalnum() or e in '._-')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if '.' not in sanitized_host:
        return {"error": "Invalid host format"}
    try:
        subprocess.run(['ping', sanitized_host], check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}