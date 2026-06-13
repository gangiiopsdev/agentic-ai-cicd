from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    for arg in args:
        if '&&' in arg or ';' in arg or '|' in arg or '`' in arg:
            raise ValueError('Invalid input detected')
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)