from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    safe_host = ''.join(c for c in host if c.isalnum() or c in '.-')
    args = ['ping', safe_host]
    subprocess.call(args)
    return {"status": "completed"}