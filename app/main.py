from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        response = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': response.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': ''}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}