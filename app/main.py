from fastapi import FastAPI
import subprocess
class PingService:
    def execute_ping(self, host: str):
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Error: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_service = PingService()
    result = ping_service.execute_ping(subprocess.escape(host))  # Add this line to sanitize the input
    return {"status": "completed", "result": result}