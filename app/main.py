from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(host):
    # Basic sanitization, improve based on actual requirements
    return ''.join(c for c in host if c.isalnum() or c in '.-')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e), 'status': 'failed'}