from fastapi import FastAPI
import subprocess
def sanitize_input(host):
    return ''.join(c for c in host if c.isalnum() or c in ['.', ':', '-', '_'])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = f'ping -c 1 {sanitized_host}'
    try:
        output = subprocess.run(sanitized_host, capture_output=True, text=True, check=True, shell=False, timeout=5)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}