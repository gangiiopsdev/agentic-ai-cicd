from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping_command(host):
    return ['ping', shlex.quote(host)]

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.check_output(ping_command(host), stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}