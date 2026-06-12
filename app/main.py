from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    try:
        subprocess.run(['ping', host], check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = execute_ping(host)
    if isinstance(result, dict) and 'error' in result:
        return result
    else:
        return {"status": "completed"}