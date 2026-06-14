from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Secure implementation using subprocess.run
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
class PingRouter:
    def __init__(self):
        pass
    def ping(self, host: str):
        return safe_ping(host)
app = FastAPI()
ping_router = PingRouter()
@app.get("/ping")
def ping_endpoint(host: str):
    result = ping_router.ping(host)
    return {"status": "completed", "result": result}