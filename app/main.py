from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    return host.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    escaped_host = escape_host(host)
    result = subprocess.run(['ping', '-c', '1', escaped_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}