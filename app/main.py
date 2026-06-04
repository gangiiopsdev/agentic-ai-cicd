from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Sanitize the host parameter
        safe_host = subprocess.list2cmdline([host])
        subprocess.run(['ping', safe_host], check=True)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    SafePing.ping(host)