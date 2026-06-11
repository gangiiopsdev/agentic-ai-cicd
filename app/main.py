from fastapi import FastAPI
import subprocess
import shlex

def escape_shell_arg(arg):
    return shlex.quote(arg)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}