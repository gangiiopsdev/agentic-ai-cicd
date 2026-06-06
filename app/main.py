from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    if not input_str.isalnum():
        raise ValueError("Invalid input")

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        output = subprocess.check_output(['ping', '-c', '1', sanitized_host], stderr=subprocess.STDOUT)
        return {"status": "completed", "output": output.decode()} if output else {"status": "failed"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}