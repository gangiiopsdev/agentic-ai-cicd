from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            result = subprocess.run(['ping', self.host], capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return str(e)

global safe_ping
safe_ping = SafePing('')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global safe_ping
    safe_ping.host = host
    result = safe_ping.execute()
    return {"status": "completed", "result": result}