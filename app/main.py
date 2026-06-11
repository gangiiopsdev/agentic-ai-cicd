from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        if not host or 'ping' in host.lower():
            raise ValueError("Invalid host")
        args = ['ping', '-c', '1', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        response = PingService.ping(host)
        return {"status": "completed", "response": response}
    except ValueError as e:
        return {"error": str(e)}