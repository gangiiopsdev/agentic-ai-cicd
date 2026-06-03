from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Safer implementation using list for the command and validate input
        args = ['ping', '-c', '4', host]
        if not all(c.isalnum() or c in '.-:' for c in host):
            raise ValueError('Invalid host name')
        subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    SafePing.ping(host)
    return {"status": "completed"}