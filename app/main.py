from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_subprocess_call(command):
    try:
        result = subprocess.run(['ping', command], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode('utf-8'))

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {"status": "error", "output": "Invalid input"}
    result = safe_subprocess_call(host)
    return {"status": "completed", "output": result}