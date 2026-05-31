from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_subprocess_call(command):
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode('utf-8'))

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_command = ['ping', host]
    result = safe_subprocess_call(safe_command)
    return {"status": "completed", "output": result}