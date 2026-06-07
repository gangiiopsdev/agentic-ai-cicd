from fastapi import FastAPI
import subprocess
def escape_host(host):
    return ''.join(e if e.isalnum() or e in '._-' else '_' for e in host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    result = subprocess.run(['ping', escaped_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}