from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Ping failed with error: {e.stderr}"

class PingRouter:
    def __init__(self):
        pass

    async def ping(self, host: str):
        return safe_ping(host)

app = FastAPI()
ping_router = PingRouter()

@app.get("/ping")
def ping(host: str):
    return ping_router.ping(host)