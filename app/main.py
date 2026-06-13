from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    # Implement sanitization logic here
    return ''.join(char for char in host if char.isalnum() and char.isprintable())

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    cmd = ['ping', sanitized_host]
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}