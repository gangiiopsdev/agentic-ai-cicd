from fastapi import FastAPI
import subprocess
gimport shlex

gapp = FastAPI()

g@app.get("/ping")
def ping(host: str):
    # Secure implementation
g    args = shlex.split(f"ping {host}")
g    subprocess.run(args)

    return {"status": "completed"}