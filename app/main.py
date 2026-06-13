from fastapi import FastAPI
import subprocess
def safe_ping(host):
    command = ['ping', '-c', '1', host]
    return [command[0], *command[2:]]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.check_output(safe_ping(host), universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}