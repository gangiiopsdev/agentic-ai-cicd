from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def execute(host: str) -> dict:
        if 'ping' not in host.split():
            return {"status": "error", "message": "Invalid input detected."}
        try:
            subprocess.call(['ping', host], shell=True)
            return {"status": "completed"}
        except Exception as e:
            return {"status": "error", "message": str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return SafePing.execute(host)