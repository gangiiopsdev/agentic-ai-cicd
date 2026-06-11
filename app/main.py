from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping_safe(host: str):
    # Enhanced validation and sanitization
    if not host.replace('.', '', 1).isdigit() or '.' not in host:
        return {'status': 'error', 'message': 'Invalid input'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}