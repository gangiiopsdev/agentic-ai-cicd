from fastapi import FastAPI
import subprocess
def run_safe_command(command):
    if isinstance(command, list) and len(command) > 0:
        try:
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output}
    else:
        raise ValueError('Invalid command format')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = ['ping', host]
    return run_safe_command(command)