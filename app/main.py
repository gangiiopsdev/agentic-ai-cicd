from fastapi import FastAPI
import subprocess
def escape_host(host):
    return ''.join(c if c.isalnum() else '_' for c in host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = escape_host(host)
    args = ['ping', safe_host]
    subprocess.run(args, check=True)
    return {"status": "completed"}