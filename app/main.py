from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run with shell=False and argument list
    result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
    return result.stdout

class PingService:
    def ping(self, host: str):
        return safe_ping(host)

@app.get("/ping")
def ping(host: str):
    ping_service = PingService()
    output = ping_service.ping(host)
    return {"status": "completed", "output": output}