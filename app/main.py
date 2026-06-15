from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def run(host):
        try:
            return subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            return str(e.output)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing()
    result = safe_ping.run(host)
    return {"status": "completed", "result": result}