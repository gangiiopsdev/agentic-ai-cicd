from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        subprocess.run(['ping', host], check=True)
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if 'command not found' in result:
        return {'status': 'error', 'message': 'Invalid command'}
    else:
        return {'status': 'completed', 'result': result}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}