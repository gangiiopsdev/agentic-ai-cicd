from fastapi import FastAPI
import subprocess
class Ping:
    @staticmethod
def safe_ping(host: str):
        # Use a list to safely pass arguments to subprocess.Popen
        args = ['ping', '-c', '1'] + [host]
        subprocess.run(args, check=True, capture_output=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    Ping.safe_ping(host)
    return {"status": "completed"}