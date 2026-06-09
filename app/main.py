from fastapi import FastAPI
import subprocess
cimport re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Prevent command injection by using safe construction
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'invalid_host'}

    subprocess.call(f"ping {host}", shell=False)
    return {'status': 'completed'}