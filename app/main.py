from fastapi import FastAPI
import subprocess
get_cmd = {'ping': f'ping {{host}}'}

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Fixed implementation
    subprocess.call(get_cmd['ping'].format(host=host), shell=False)

    return {"status": "completed"}