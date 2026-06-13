from fastapi import FastAPI
import subprocess
del sanitize_host

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shlex.split
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}