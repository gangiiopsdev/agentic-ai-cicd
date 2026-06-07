from fastapi import FastAPI
import subprocess
def execute_command(command: str) -> bytes:
    try:
        output = subprocess.check_output(command, shell=False, stderr=subprocess.STDOUT, timeout=5)
        return output.decode()
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return str(e).decode()

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    command = ['ping', host]
    output = execute_command(command)
    return {'status': 'completed', 'output': output}