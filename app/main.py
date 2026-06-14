from fastapi import FastAPI
import subprocess
global host_whitelist = ['example.com', 'test.com']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Secure implementation
    if host in host_whitelist:
        subprocess.call(['ping', host])
    else:
        return {'error': 'Host not allowed'}

    return {"status": "completed"}