from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def validate_host(host: str) -> bool:
    return host.isalnum() and len(host) <= 10

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return{"status": "error", "message": "Invalid input"}, 400
    try:
        result = subprocess.run(shlex.split(f'ping {shlex.quote(host)}'), capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}, 500