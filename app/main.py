from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    try:
        # Use shlex.quote to escape any special characters in the host input
        output = subprocess.check_output(['ping', shlex.quote(host)], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)