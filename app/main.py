from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        args = ["ping"] + shlex.split(host)
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}
    return {"status": "completed", "output": output.decode()}