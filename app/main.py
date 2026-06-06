from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

class FastApiPing:
    def __init__(self):
        self.app = app

    async def ping(self, host: str):
        try:
            # Use shlex to safely escape the input
            safe_host = shlex.quote(host)
            output = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

global fastapi_ping
fastapi_ping = FastApiPing()

@app.get("/ping")
def ping(host: str):
    return fastapi_ping.ping(host)