from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.isalnum():
        args = shlex.split('ping ' + host)
        subprocess.call(args)
        return {"status": "completed"}
    else:
        return {"error": "Invalid input"}