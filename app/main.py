from fastapi import FastAPI
import subprocess
cimport os
def safe_ping(host: str):
    if not all(char.isalnum() or char in ['.', '-'] for char in host):
        raise ValueError('Invalid hostname')
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout,

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        return safe_ping(host)
    except ValueError as e:
        return {"error": str(e)}, 400