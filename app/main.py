from fastapi import FastAPI
import subprocess
def execute_safe_command(command_parts):
    try:
        subprocess.run(command_parts, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Command failed with error {e}')
        return False

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command_parts = ['ping', host]
    if execute_safe_command(command_parts):
        return {"status": "completed"}
    else:
        return {"status": "failed"}