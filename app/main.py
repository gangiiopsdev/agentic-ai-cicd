from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    return ''.join(c for c in host if c.isalnum() or c in '.-:=')

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    try:
        escaped_host = escape_host(host)
        output = subprocess.check_output(['ping', '-c', '1', escaped_host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}