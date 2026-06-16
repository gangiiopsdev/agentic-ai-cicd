from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_ping(host: str):
    command = ['ping', host]
    args = shlex.split(' '.join(command))
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    secure_ping(host)
    return {"status": "completed"}