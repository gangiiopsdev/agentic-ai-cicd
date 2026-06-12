from fastapi import FastAPI
import subprocess
def escape_host(host):
    return ''.join(c if c.isalnum() else '_' for c in host)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    args = ['ping', '-c', '1', escaped_host]
    subprocess.run(args, check=True, capture_output=True, text=True)
    return {"status": "completed"}