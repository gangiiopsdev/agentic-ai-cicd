from fastapi import FastAPI
import subprocess
def sanitize_input(host: str):
    return ''.join(c for c in host if c.isalnum() or c in '-_.,/\')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.run(['ping', f'-c 4 {sanitized_host}'], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}