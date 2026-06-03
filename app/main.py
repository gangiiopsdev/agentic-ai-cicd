from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    # Sanitize input to prevent command injection
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True, shell=False)
    return result.stdout

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # More robust validation to prevent command injection
    if not host.isalnum() and not all(c in '0123456789.' for c in host):
        return {'status': 'error', 'message': 'Invalid input'}
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}