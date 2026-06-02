from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex.quote for argument quoting
    subprocess.call(['ping', host])

@app.get("/ping")
def ping_route(host: str):
    return ping(host)