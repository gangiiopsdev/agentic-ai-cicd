from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input before using it in the subprocess call
    if ' ' not in host:
        subprocess.run(['ping', shlex.quote(host)], check=True)
    else:
        raise ValueError('Invalid input detected')
    return {"status": "completed"}