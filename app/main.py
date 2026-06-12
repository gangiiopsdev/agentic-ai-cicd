from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    for arg in args:
        if isinstance(arg, str) and '&&' in arg or ';' in arg:
            raise ValueError('Invalid characters in argument')
    subprocess.run(args, check=True, timeout=5)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)