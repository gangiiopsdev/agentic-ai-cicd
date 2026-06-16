from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_ping(host):
    # Secure implementation using subprocess.run instead of subprocess.call
    try:
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    return execute_ping(host)

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}