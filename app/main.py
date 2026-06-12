from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def safe_ping(host: str):
        try:
            return subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            return e.output

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    safe_host = subprocess.quote(host)
    result = PingCommand.safe_ping(safe_host)
    return {"status": "completed", "result": result}