from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and arg validation
    if host.strip().replace('.', '').isnumeric() and 1 <= int(host.split('.')[0]) <= 254:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"error": "Invalid or non-IP address provided"}