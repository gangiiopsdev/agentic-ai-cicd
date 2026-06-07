from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def run(host: str) -> dict:
        try:
            subprocess.run(["ping", host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {"status": "completed"}
        except subprocess.CalledProcessError as e:
            return {"error": str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return SafePing.run(host)