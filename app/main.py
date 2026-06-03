from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Validate and sanitize the host input
        if not isinstance(host, str) or not all(c.isalnum() or c in ('.', '-', '_') for c in host):
            raise ValueError('Invalid host name')
        args = ['ping', host]
        subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    SafePing.ping(host)
    return {"status": "completed"}