from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False
    try:
        subprocess.run(f'ping {host}', shell=False, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

    return {'status': 'completed'}