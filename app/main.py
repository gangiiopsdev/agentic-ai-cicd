from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, host):
        self.host = host

    def safe_ping(self):
        args = ['ping', '-c', '1', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

global ping_instance
ping_instance = SafePing(host='')

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get(
    "/ping",
    dependencies=[Depends(ping_instance.safe_ping)]
)
def ping(host: str):
    ping_instance.host = host
    return ping_instance.safe_ping()