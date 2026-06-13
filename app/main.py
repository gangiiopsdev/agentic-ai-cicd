from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent command injection
    safe_host = ''.join(c for c in host if c.isalnum() or c in '.-')
    args = ['ping', safe_host]
    subprocess.run(args, check=True)
    return {"status": "completed"}