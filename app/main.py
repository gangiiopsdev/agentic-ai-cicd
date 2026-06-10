from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        args = ['ping', host]
        try:
            subprocess.run(args, check=True)
        except subprocess.CalledProcessError as e:
            raise ValueError(f'Failed to ping {host}: {e}')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        SafePing.safe_ping(host)
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e)}