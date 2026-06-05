from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_argument(arg):
    return ''.join(c if c.isalnum() or c in '._-' else '_' for c in arg)

@app.get("/ping")
def ping(host: str):
    safe_host = escape_shell_argument(host)
    subprocess.call(f"ping {safe_host}", shell=True)
    return {"status": "completed"}