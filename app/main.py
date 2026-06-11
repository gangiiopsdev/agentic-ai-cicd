from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
    args = ['ping'] + shlex.split(host)
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    return ping(host)