from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    try:
        result = subprocess.run(['ping', *shlex.split(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate host input to prevent command injection
    if not host.replace('.', '').isalnum():
        return {'status': 'error', 'error': 'Invalid input'}
    return ping(host)