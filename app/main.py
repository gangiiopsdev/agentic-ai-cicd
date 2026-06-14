from fastapi import FastAPI
import subprocess
class PingSafe:
    @staticmethod
def ping(host: str):
        return subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = PingSafe.ping(host)
    return {"status": result.returncode, "stdout": result.stdout}