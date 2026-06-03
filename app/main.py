from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(filter(lambda x: x.isalnum() or x in '.-/', input_string))

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)
    return {"status": "completed", "output": subprocess.run(['ping', sanitized_host]).stdout}