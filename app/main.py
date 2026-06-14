from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    args = ['ping', host]
    for arg in args:
        if isinstance(arg, str) and any(char in arg for char in ('&&', ';', '|', '`')):
            raise ValueError('Invalid characters in argument')
    subprocess.run(args, check=True, timeout=5)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(shlex.quote(host))