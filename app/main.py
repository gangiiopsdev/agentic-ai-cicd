from fastapi import FastAPI
import subprocess
def secure_ping(host: str):
    if not host.isdigit() or len(host) > 3:
        raise ValueError('Invalid input')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return secure_ping(host)