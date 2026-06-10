from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}