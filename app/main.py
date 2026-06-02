from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host: str):
    return ''.join(char for char in host if char.isalnum() or char in ('.', '-', '_'))

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    subprocess.call(f"ping {escaped_host}", shell=False)
    return {"status": "completed"}