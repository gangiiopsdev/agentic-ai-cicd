from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    return ''.join(e if e.isalnum() or e in '.-' else '_' for e in host)

@app.get("/ping")
def ping(host: str):
    safe_host = escape_host(host)
    try:
        subprocess.run(['ping', safe_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}