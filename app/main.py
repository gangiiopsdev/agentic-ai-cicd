from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    if not input_str.isalnum() or '.' in input_str:
        raise ValueError('Invalid host')
    return input_str.replace(';', '').replace('&', '')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    subprocess.run(['ping', host], check=True, shell=False)
    return {"status": "completed"}