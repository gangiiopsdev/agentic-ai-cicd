from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize host input
    if ' ' in host or ';' in host or '&' in host or '|' in host:
        return {'error': 'Invalid host input'}
    subprocess.call(["ping", subprocess.check_output(['echo', host]).decode().strip()])
    return {"status": "completed"}