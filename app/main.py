from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        if not host.isalnum():
            return "Invalid input"
        args = ['ping', '-c', '4', host]
        subprocess.run(args, capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = SafePing.ping(host)
    return {"status": result}