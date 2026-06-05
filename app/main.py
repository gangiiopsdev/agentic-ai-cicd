from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'success', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(host)