from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
    command = ['ping', host]
    args = ' '.join(shlex.quote(arg) for arg in command)
    subprocess.run(args, shell=True, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)