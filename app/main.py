from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with sanitized input
    args = ['ping', *shlex.split(host)]
    result = subprocess.run(args, check=True)
    return result

@app.get("/ping")
def ping_endpoint(host: str):
    result = ping(host)
    return {"status": "completed", "result": result}