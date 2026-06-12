from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def _ping(host):
    args = shlex.split(f'ping {host}')
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    try:
        if not host.isdigit():  # Example validation, adjust as needed
            raise ValueError('Invalid input')
        _ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}