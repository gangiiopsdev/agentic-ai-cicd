from fastapi import FastAPI
import shlex
class SafePing:
    @staticmethod
def ping(host: str):
        # Sanitize the host parameter
        safe_host = shlex.quote(host)
        subprocess.run(['ping', safe_host], check=True)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    SafePing.ping(host)