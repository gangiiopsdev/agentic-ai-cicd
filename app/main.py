from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    return ''.join(char if char.isalnum() or char in ('.', '-', '_') else '_' for char in host)

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    subprocess.call(f"ping {escaped_host}", shell=False)
    return {"status": "completed"}