from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], universal_newlines=True, timeout=5)
        return output
    except subprocess.CalledProcessError as e:
        return str(e)

def safe_execute(command: list):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True, timeout=5)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    result = safe_execute(['ping', host])
    return {'status': 'completed', 'result': result}