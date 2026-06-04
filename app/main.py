from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    args = ['ping'] + shlex.split(host)
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    output, error = safe_ping(host)
    if error:
        return {"status": "error", "output": output, "error": error}
    else:
        return {"status": "completed", "output": output}