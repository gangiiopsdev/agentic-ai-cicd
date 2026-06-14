from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        args = ['ping', shlex.quote(host)]
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=10)
        return {"status": "completed", "output": output.decode()}  # Return ping output if needed
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e.output)}