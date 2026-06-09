from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', host]
    # Ensure the host input does not contain any potentially harmful characters
    if '/' in host or '@' in host:
        raise ValueError('Invalid host name')
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}