from fastapi import FastAPI
import subprocess
def shell_exec(command: str):
    try:
        output = subprocess.check_output(command.split(), stderr=subprocess.STDOUT, timeout=10)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command = f'ping -c 1 {host}'
    return shell_exec(command)