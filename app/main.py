from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Ping failed with error: {e}

global_ping_service = PingService()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return global_ping_service.ping(host)