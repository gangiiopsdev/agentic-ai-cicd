from fastapi import FastAPI
import subprocess
def execute_ping(host):
    # Secure implementation using subprocess.run
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
class PingService:
    def ping(self, host: str):
        return execute_ping(host)
app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    response = ping_service.ping(host)
    return {'status': 'completed', 'result': response}