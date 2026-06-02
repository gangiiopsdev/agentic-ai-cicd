from fastapi import FastAPI
import subprocess
global host whitelist = ['example.com', 'test.com']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in global_host_whitelist:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
    else:
        return {'status': 'error', 'message': 'Host not allowed'}