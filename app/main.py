from fastapi import FastAPI
import subprocess

def escape_host(host):
    return ''.join(c for c in host if c.isalnum() or c in '._-')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = escape_host(host)
    args = ['ping', '--'] + safe_host.split()
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}