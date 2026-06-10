from fastapi import FastAPI
import subprocess
def sanitize_input(host):
    return ''.join(c for c in host if c.isalnum() or c in ['.', ':', '-', '_'])

cmd = ['ping', '-c 1', sanitized_host]

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=5)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}