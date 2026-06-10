from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_argument(arg):
    arg = str(arg)
    return ''.join(c if c.isalnum() else '_' for c in arg)

@app.get("/ping")
def ping(host: str):
    host = escape_shell_argument(host)
    subprocess.call(["ping", host], shell=False)

    return {"status": "completed"}