from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        output = subprocess.check_output(shlex.split(f'ping {host}'), timeout=5, stderr=subprocess.STDOUT)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}
    except subprocess.TimeoutExpired:
        return {"status": "timeout"}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)