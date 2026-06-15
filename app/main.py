from fastapi import FastAPI
import subprocess

def execute_safe_command(command_parts):
    try:
        result = subprocess.run(command_parts, check=True, capture_output=True, text=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        print(f'Command failed with error {e}')
        return False, e.stderr

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if 'localhost' not in host and '127.0.0.1' not in host:
        return {'status': 'failed'}
    command_parts = ['ping', host]
    success, output = execute_safe_command(command_parts)
    if success:
        return {'status': 'completed', 'output': output}
    else:
        return {'status': 'failed', 'error': output}