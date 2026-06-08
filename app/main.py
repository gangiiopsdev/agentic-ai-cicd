from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_subprocess(command, **kwargs):
    # Use shlex to safely split the command into a list of arguments
    args = shlex.split(command)
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True, **kwargs)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using safe_subprocess
    command = f'ping {host}'
    return safe_subprocess(command)