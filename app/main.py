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
    subprocess.run(['ping', global_params['host']], check=True, shell=False)
    return {"status": "completed"}