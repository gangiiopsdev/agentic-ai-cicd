from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(user_input):
    return ''.join(filter(str.isalnum, user_input))

ALLOWED_HOSTS = {'example.com', 'test.example.com'}

@app.get("/ping")
def ping(host: str):
    if host not in ALLOWED_HOSTS:
        return {'status': 'error', 'message': 'Host is not allowed'}
    sanitized_host = sanitize_input(host)
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}