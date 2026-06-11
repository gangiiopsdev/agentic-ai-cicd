from fastapi import FastAPI
import subprocess
global host_whitelist = ['example.com', 'test.com']

app = FastAPI()

def ping(host: str):
    if host not in host_whitelist:
        return {'status': 'failed', 'error': 'Host is not allowed'}
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.output)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)