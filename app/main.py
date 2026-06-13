from fastapi import FastAPI
import subprocess
def execute_safe_command(command):
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return f'Error: {e.output}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to avoid injection attacks
    if not host.isalnum() or len(host) > 255:
        return {"error": "Invalid host name"}
    command = ['ping', host]
    result = execute_safe_command(command)
    return {"status": "completed", "result": result}