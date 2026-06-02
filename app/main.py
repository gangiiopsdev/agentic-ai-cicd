from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_ping(host):
    try:
        args = shlex.split('ping ' + host)
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    return execute_ping(host)