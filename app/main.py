from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with shell=False and splitting the command properly
    try:
        subprocess.run(shlex.split('ping ' + host), check=True, shell=False)
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}
    return {"status": "completed"}