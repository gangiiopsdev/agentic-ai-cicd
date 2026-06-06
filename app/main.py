from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        # Validate and sanitize input
        if not host.isalnum():
            raise ValueError("Invalid host")
        # Use a parameterized command to avoid shell injection
        command = ['ping', '-c', '1', host]
        # Execute the command safely without using shell=True
        subprocess.run(command, check=True, shell=False)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    SafePing.safe_ping(host)