from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(value: str) -> str:
    return ''.join(filter(str.isalnum, value))

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', sanitized_host]
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        return {'status': 'failed', 'error': result.stderr}
    return {'status': 'completed'}