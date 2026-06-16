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
    if not all(c.isdigit() or c == '.' for c in host) or len(host.split('.')) != 4:
        raise ValueError("Invalid host format")
    result = PingSafe.ping(host)
    return {"status": result.returncode, "stdout": result.stdout}