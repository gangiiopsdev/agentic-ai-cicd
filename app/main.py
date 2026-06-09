from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex.quote
    from shlex import quote
    subprocess.call(f'ping {quote(host)}', shell=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)