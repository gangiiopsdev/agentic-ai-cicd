from fastapi import FastAPI
import subprocess
import shlex
def execute_ping(host):
    try:
        # Using subprocess.run instead of subprocess.call for better security and more features
        result = subprocess.run(['ping'] + [arg.strip() for arg in host.split()], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if all(c.isalnum() or c in '.-_' for c in host):  # Simple validation to prevent injection
        return execute_ping(host)
    else:
        return {'status': 'failed', 'error': 'Invalid input'}