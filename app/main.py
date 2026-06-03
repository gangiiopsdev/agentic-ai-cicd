from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    if not input_str.isalnum():
        raise ValueError("Input contains non-alphanumeric characters")

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        sanitize_input(host)
        subprocess.run(['ping', '-c 1', host], check=True)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}, 400