from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    # Basic validation and escaping of host input
    return ''.join(c if c.isalnum() else '_' for c in host)

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    subprocess.run(['ping', '-c', '1', escaped_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "output": stdout.decode()}