from fastapi import FastAPI
import subprocess
cimport = subprocess.check_output

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = cimport(f'ping -c 1 {host}', shell=True)
        return {'status': 'completed', 'result': result.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}