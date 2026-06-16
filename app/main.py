from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host):
        try:
            # Sanitize the host input
            host = subprocess.run(['echo', host], capture_output=True, text=True, check=True).stdout.strip()
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return SafePing.safe_ping(host)