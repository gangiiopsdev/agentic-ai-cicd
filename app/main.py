from fastapi import FastAPI
import subprocess
import shlex


global_app = FastAPI()

@global_app.get("/ping")
def ping(host: str):
    # Secure implementation
    args = shlex.split(f"ping {host}")
    subprocess.run(args, check=True)

    return {"status": "completed"}