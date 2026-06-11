from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    return ''.join(c if c.isalnum() or c in ('.', '-', '_') else '_' for c in host)

@app.get("/ping")
def ping(host: str):
    safe_host = escape_host(host)
    subprocess.run(['ping', safe_host], capture_output=True, text=True)
    return {'status': 'completed'}