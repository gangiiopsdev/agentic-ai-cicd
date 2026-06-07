from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    return ''.join(char for char in host if char.isalnum() or char in ('.', '-'))

@app.get("/ping")
def ping(host: str):
    safe_host = escape_host(host)
    subprocess.call(f"ping {safe_host}", shell=False)
    return {"status": "completed"}