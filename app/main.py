from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def safe_ping(host: str):
        # Define a whitelist of allowed hosts
        allowed_hosts = ['example.com', 'localhost']
        if host in allowed_hosts:
            command = ['ping', host]
            subprocess.call(command)

app = FastAPI()

@app.get("/" perpetate the fix.")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    PingCommand.safe_ping(host)
    return {"status": "completed"}