from fastapi import FastAPI
import subprocess
import shlex
def escape_host(host):
    return ''.join(c for c in host if c.isalnum() or c in '-._')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        safe_host = escape_host(host)
        result = subprocess.run(shlex.split(f'ping {safe_host}'), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": str(e)}