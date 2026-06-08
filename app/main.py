from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host):
    return shlex.quote(host)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host.isdigit() or len(sanitized_host) > 15:
        return {"status": "failed", "error": "Invalid input"}
    try:
        result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}