from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host):
        try:
            # Use the ping -c command on Unix-like systems or ping -n on Windows
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    response = SafePing.safe_ping(host)
    return {"status": "completed", "response": response}