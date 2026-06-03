from fastapi import FastAPI
import subprocess
global_params = {
    'ping': ['-c', '1'],
    # Add more commands as needed
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
    # Basic validation to prevent command injection
    if not host.isalnum():
        return {'status': 'error', 'output': 'Invalid input'}
    # Use subprocess.run with parameterized arguments to avoid command injection
    output = run_command(['ping'] + ['-' * 32] + [host])
    return {'status': 'completed', 'output': output}