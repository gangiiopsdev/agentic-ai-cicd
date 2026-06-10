from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_arg(arg):
    return ''.join(c if c.isalnum() else '_' for c in arg)

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_shell_arg(host)
    subprocess.call(f"ping {escaped_host}", shell=True)
    return {"status": "completed"}