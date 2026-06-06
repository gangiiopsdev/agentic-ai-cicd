from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host not in ["google.com", "example.com"]:
        raise ValueError("Invalid host")
    args = shlex.split('ping ' + host)
    subprocess.run(args, check=True)
    return {"status": "completed"}