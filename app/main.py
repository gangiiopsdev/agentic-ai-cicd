from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        if 'ping' in host or any(char.isalnum() for char in host):
            raise ValueError('Invalid input')
        subprocess.call(['ping', host])
app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    SafePing.ping(host)
    return {"status": "completed"}