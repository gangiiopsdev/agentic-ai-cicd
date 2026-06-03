from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return ping(host)