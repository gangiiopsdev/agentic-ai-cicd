from fastapi import FastAPI
import subprocess
def validate_host(host):
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        return False
    return True
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"error": "Invalid input"}, 400
    subprocess.call(["ping", host], shell=False)
    return {"status": "completed"}