from fastapi import FastAPI
import subprocess

def execute_ping(host):
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return output.stdout.strip()
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host == 'localhost' or host == '127.0.0.1':
        return execute_ping(host)
    else:
        return "Invalid host"