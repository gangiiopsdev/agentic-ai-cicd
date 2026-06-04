from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    @staticmethod
def ping(host: str):
        try:
            safe_host = shlex.quote(host)
            result = subprocess.run(["ping", safe_host], check=True, shell=False)
            return {"status": "completed"}
        except subprocess.CalledProcessError as e:
            return {"status": "error", "message": str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return SafePing.ping(host)