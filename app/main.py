from fastapi import FastAPI
import subprocess
def escape_host(host):
    return ''.join(c if c.isalnum() or c in ['-', '.', '_'] else '_' for c in host)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_host = escape_host(host)
    try:
        output = subprocess.check_output(['ping', safe_host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}