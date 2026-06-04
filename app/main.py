from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    # Basic sanitization, in production, consider using regex or a whitelist
    return ''.join(filter(str.isalnum, host))

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    args = ['ping', sanitized_host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}