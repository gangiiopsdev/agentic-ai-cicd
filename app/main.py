from fastapi import FastAPI
import subprocess
global_params = {'host': ''}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global_params['host'] = host
    # Safe implementation
    subprocess.call(['ping', global_params['host']], shell=False)
    return {"status": "completed"}