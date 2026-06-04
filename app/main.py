from fastapi import FastAPI
import subprocess
class SafePinger:
    @staticmethod
def ping(host: str):
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    pinger = SafePinger()
    return pinger.ping(host)