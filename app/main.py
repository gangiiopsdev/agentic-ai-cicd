from fastapi import FastAPI
import subprocess
def execute_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    allowed_hosts = ['localhost', '127.0.0.1']
    if host in allowed_hosts:
        command = ["ping", host]
        result = execute_command(command)
        return {"status": "completed", "result": result}
    else:
        return {"status": "error", "message": "Invalid host"}