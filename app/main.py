from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_ping(host: str):
    if 'ping' not in host:
        command = f'ping -c 4 {host}'
        try:
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr.decode()}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return secure_ping(host)