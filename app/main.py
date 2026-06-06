from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run and shlex.quote
    from shlex import quote
    subprocess.run(['ping', quote(host)])

@app.get="/ping")
def ping_route(host: str):
    return ping(host)