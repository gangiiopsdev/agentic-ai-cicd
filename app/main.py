from fastapi import FastAPI
import subprocess
def shell_escape(s):
    return ''.join(c for c in s if c.isalnum() or c in (' ', '.', '-', '_', '@'))
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    safe_host = shell_escape(host)
    try:
        output = subprocess.check_output(['ping', safe_host], stderr=subprocess.STDOUT, universal_newlines=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output}