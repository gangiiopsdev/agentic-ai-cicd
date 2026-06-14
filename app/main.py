from fastapi import FastAPI, HTTPException
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            result = subprocess.run(['ping', self.host], check=True, capture_output=True, text=True)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            raise HTTPException(status_code=400, detail=str(e))
global_ping_command = PingCommand(None)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        raise HTTPException(status_code=400, detail="Invalid input")
    global_ping_command.host = host
    return global_ping_command.execute()