from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def safe_ping(host: str) -> int:
        try:
            return subprocess.call(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except Exception as e:
            print(f'Error pinging {host}: {e}')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = PingCommand.safe_ping(host)
    if result == 0:
        return {"status": "completed", "response": "Success"}
    else:
        return {"status": "failed", "response": "Failed"}