from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run and shlex.quote
    subprocess.run(['ping', shlex.quote(host)], check=True)
    return {"status": "completed"}