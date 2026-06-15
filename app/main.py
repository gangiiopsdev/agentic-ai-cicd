from fastapi import FastAPI
import subprocess
def run_ping(host):
    try:
        response = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return response.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = subprocess.quote(host)
    command = ['ping', '-c', '1'] + [sanitized_host]
    response = subprocess.run(command, capture_output=True, text=True, check=True)
    return response.stdout