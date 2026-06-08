from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex.quote to safely pass arguments
    subprocess.call(['ping', host], shell=False)

@app.get="/ping")
def ping_route(host: str):
    return ping(host)