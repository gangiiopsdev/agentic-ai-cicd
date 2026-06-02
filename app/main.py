from fastapi import FastAPI
import subprocess
def escape_host(host: str):
    return ''.join(c if c.isalnum() or c in '._-' else '_' for c in host)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_host(host)
    subprocess.run(['ping', '-c', '1', escaped_host], check=True, capture_output=True, text=True)
    return {'status': 'completed'}