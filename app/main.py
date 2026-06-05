from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        # Safe implementation using subprocess.run
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_service = PingService()
    return {'status': 'completed', 'output': ping_service.ping(host)}