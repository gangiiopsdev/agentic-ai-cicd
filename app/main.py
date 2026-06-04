from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        # Validate and sanitize input
        if not host.isalnum():
            raise ValueError("Invalid host")
        command = ['ping', '-c', '1', host]
        subprocess.run(command, check=True)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return SafePing.safe_ping(host)