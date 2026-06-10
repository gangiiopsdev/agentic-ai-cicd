from fastapi import FastAPI
import subprocess
class PingService:
    def safe_execute(self, command: list):
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    command = ['ping', host]
    return {'status': 'completed', 'output': ping_service.safe_execute(command)}