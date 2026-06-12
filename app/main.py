from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    return ''.join(c for c in host if c.isalnum() or c in ('.', '-', '_'))

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    result = subprocess.run(['ping', '-c', '1', escaped_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}