from fastapi import FastAPI
import subprocess
def execute_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

cmd_app = FastAPI()

cmd_app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

cmd_app.get("/ping")
def ping(host: str):
    safe_command = ['ping', '-c', '1', host]
    result = execute_command(safe_command)
    return {"status": "completed", "result": result}