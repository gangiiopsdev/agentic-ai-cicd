from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Ensure the host does not contain any shell metacharacters
        safe_host = subprocess.list2cmdline([host])
        subprocess.call(['ping', safe_host])
app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    SafePing.ping(host)
    return {"status": "completed"}