from fastapi import FastAPI
import subprocess
def execute_command(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True, shell=False)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command = ['ping', host]
    if ' ' in host or '"' in host or '\' in host:
        return {'error': 'Invalid input'}
    return {'output': execute_command(command)}