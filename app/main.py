from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not all(c.isalnum() or c in '._-' for c in host):
        return {'status': 'error', 'message': 'Invalid input'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode('utf-8'))

# Use a safer approach by constructing the command in a secure way
@app.get("/ping_safe")
def ping_safe(host: str):
    if not all(c.isalnum() or c in '._-' for c in host):
        return {'status': 'error', 'message': 'Invalid input'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode('utf-8'))