from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    return ''.join(c if c.isalnum() else '_' for c in host)

@app.get("/ping")
def ping(host: str):
    # Escaped implementation
    subprocess.call(f"ping {escape_host(host)}", shell=False)

    return {"status": "completed"}