from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        # Safe implementation without shell=True
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():  # Prevents command injection by ensuring only alphanumeric characters are allowed
        raise ValueError("Invalid input")
    return PingService.ping(host)