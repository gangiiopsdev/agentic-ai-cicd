from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    return host.isalnum()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}