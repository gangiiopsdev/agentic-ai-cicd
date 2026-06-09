from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Validate input
        if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
            raise ValueError("Invalid hostname")
        args = ['ping', host]
        subprocess.call(args)
app = FastAPI()
@app.get("/ping")
def ping_endpoint(host: str):
    SafePing.ping(host)
    return {"status": "completed"}