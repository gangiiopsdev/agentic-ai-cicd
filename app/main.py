from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Safe implementation
    command = ['ping', host]
    subprocess.call(command, shell=False)

@app.get("/ping")
def ping_endpoint(host: str):
    result = ping(host)
    return {"status": "completed", "result": result}