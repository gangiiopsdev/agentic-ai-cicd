from fastapi import FastAPI
import subprocess
def validate_host(host: str) -> bool:
    return all(c.isalnum() or c in ('.', '-') for c in host)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "error", "message": "Invalid host"}
    subprocess.call(["ping", f'"{host}"'], shell=False)

    return {"status": "completed"}