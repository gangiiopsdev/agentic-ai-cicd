from fastapi import FastAPI
import subprocess
def execute_command(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Preventive controls
    if host.replace('.', '').isnumeric() and len(host.split('.')) == 4:
        command = ['ping', host]
        return {'output': execute_command(command)}
    else:
        return {'error': 'Invalid hostname'}