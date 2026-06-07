from fastapi import FastAPI
import subprocess
import shlex
def escape_host(host):
    return ''.join(c for c in host if c.isalnum() or c in '-._')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    try:
        result = subprocess.run(shlex.split(f"ping {escaped_host}"), check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}