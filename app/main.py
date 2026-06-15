from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_wrapper(host: str):
    if not validate_host(host):
        return {'status': 'invalid', 'message': 'Invalid host'}
    return ping(host)

def validate_host(host: str) -> bool:
    # Simple validation example, replace with more robust validation logic
    return '.' in host