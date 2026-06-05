from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with shell=False and use of shlex.quote to escape user input
    command = ['ping', shlex.quote(host)]
    result = subprocess.run(command, check=True, capture_output=True)
    return {"status": "completed", "output": result.stdout.decode()}