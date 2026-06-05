from fastapi import FastAPI
import subprocess

global_params = {
    'ping': ['-c', '1'],
}

def run_command(command):
    try:
        result = subprocess.run(command, check=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Enhanced validation to prevent command injection
    if not host.isalnum() or len(host) > 64:
        return {'status': 'error', 'output': 'Invalid input'}
    # Use subprocess.run with parameterized arguments to avoid command injection
    output = run_command(['ping'] + global_params['ping'] + [host])
    return {'status': 'completed', 'output': output}