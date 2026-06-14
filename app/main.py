from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if host.strip():
        args = ['ping', host]
        subprocess.run(args, check=True)
    return {'status': 'completed'}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)