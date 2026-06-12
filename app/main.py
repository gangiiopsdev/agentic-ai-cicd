from fastapi import FastAPI
import subprocess
def execute_command(cmd):
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host.strip() != host:
        return {"error": "Invalid input"}
    cmd = ['ping', subprocess.check_output([host]).decode().strip()]
    result = execute_command(cmd)
    return {'status': 'completed', 'result': result}