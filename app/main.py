from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    return all(c not in host for c in [';', '&', '\'])

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'error', 'message': 'Invalid input'}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'result': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output.decode('utf-8')}"