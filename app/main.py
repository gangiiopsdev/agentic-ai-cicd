from fastapi import FastAPI
import subprocess
def escape_host(host):
    return host.replace(';', '').replace('&', '').replace('|', '')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    result = subprocess.run(['ping', escaped_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}