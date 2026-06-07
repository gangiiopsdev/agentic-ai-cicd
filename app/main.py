from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run instead of subprocess.call
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True)
    return result

@app.get('/ping')
def ping(host: str):
    # Using a safe function to avoid injection
    try:
        response = safe_ping(host)
        return {'status': 'completed', 'output': response.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}