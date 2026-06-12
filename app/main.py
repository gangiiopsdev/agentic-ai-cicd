from fastapi import FastAPI
import subprocess
import shlex

class HostValidator:
    @staticmethod
def is_valid_host(host: str) -> bool:
        return all(c.isalnum() or c in '.:-' for c in host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not HostValidator.is_valid_host(host):
        return {"error": "Invalid host"}, 400
    args = shlex.split('ping ' + host)
    subprocess.call(args)
    return {"status": "completed"}