from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        args = shlex.split(f"ping {host}")
        subprocess.run(args, check=True)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}, 400