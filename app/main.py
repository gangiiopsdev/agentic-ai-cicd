from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Command failed: {e}'

@app.get("/ping")
def ping(host: str):
    command = ['ping', host]
    return {'status': execute_command(command)}