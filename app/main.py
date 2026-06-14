from fastapi import FastAPI
import subprocess
from shlex import quote as cmd_quote

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or '..' in host:
        return {"status": "error", "output": "Invalid input"}
    try:
        result = subprocess.run(['ping', cmd_quote(host)], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e)}