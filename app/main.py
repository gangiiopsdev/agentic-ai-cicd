from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_host(host):
    # Simple escaping to prevent common injections
    return ''.join(c for c in host if c.isalnum() or c in ('.', '-', '_', '/'))

@app.get("/ping")
def ping(host: str):
    escaped_host = shlex.quote(escape_host(host))
    subprocess.run(['ping', escaped_host], check=True, shell=False)
    return {"status": "completed"}