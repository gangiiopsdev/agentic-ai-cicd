from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_command(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using shlex.quote to prevent command injection
    command = ['ping', shlex.quote(host)]
    return run_command(command)