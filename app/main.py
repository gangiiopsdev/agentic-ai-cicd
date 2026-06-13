from fastapi import FastAPI
import subprocess
class SafePinger:
    def ping(self, host: str):
        subprocess.run(['ping', '-c', '1', host], check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    pinger = SafePinger()
    try:
        pinger.ping(host)
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}
    return {"status": "completed"}