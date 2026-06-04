from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {"status": "failed", "error": "Invalid input"}
    args = ['ping', host]
    output = subprocess.run(args, stderr=subprocess.STDOUT, capture_output=True, text=True)
    return {"status": "completed", "output": output.stdout}