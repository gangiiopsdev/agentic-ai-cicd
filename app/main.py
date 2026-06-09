from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        if not host or ' ' in host or ';' in host or '&' in host:
            raise ValueError('Invalid input')
        subprocess.call(['ping', host])

app = FastAPI()

@app.get("/ping")
def ping_handler(host: str):
    SafePing.ping(host)
    return {"status": "completed"}