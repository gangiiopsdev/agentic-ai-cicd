from fastapi import FastAPI
import subprocess
class PingService:
    def ping(host: str):
        # Safe implementation without shell=True
        subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    service = PingService()
    return {'status': 'completed'}