from fastapi import FastAPI
import subprocess
def sanitize_input(input):
    return ''.join(e for e in input if e.isalnum() or e in '.-: ')  # Allow alphanumeric and some special characters

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}