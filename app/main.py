from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        # Secure implementation
        args = ['ping', '-c', '4', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()
ping_service = PingService()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    response = ping_service.ping(host)
    return {"status": "completed", "output": response}