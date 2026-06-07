from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        args = shlex.split(f"ping {host}")
        subprocess.call(args)
    except Exception as e:
        return {'error': str(e)}

@app.get("/ping")
def ping(host: str):