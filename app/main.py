from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        # Validate and sanitize input
        if not host.isalnum():
            raise ValueError("Invalid host")
        command = ['ping', '-c', '1', host]
        # Use a safe method to execute the command
        subprocess.run(command, check=True)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    SafePing.safe_ping(host)