from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.isnumeric():
        return {"error": "Invalid input. Host must be numeric."}
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    
    return {"status": "completed"}