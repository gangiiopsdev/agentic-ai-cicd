from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host: str) -> str:
    # Basic sanitization to prevent certain characters
    return ''.join(c for c in host if c.isalnum() or c in ['-', '.', ' ', '_'])

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    args = ['ping', sanitized_host]
    result = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = result.communicate()
    return {'status': 'completed'}