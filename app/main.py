from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping', host]
    subprocess.run(args, check=True)

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent injection attacks
    sanitized_host = ''.join(e for e in host if e.isalnum() or e in ['.', '-', '_'])
    safe_ping(sanitized_host)
    return {"status": "completed"}