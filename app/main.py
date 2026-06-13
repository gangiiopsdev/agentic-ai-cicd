from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with shlex for safe command argument handling
    try:
        args = ['ping', '-c', '1'] + shlex.split(host)
        output = subprocess.check_output(args, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}