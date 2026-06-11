from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(host: str):
    return ''.join(c for c in host if c.isalnum() or c in '-_.,/\')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.check_output(['ping', f'-c 4 {sanitized_host}'], stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}