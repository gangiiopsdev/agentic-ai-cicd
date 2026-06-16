from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.safe_hosts = ['example.com']  # List of allowed hosts

    def safe_ping(self, host):
        if host in self.safe_hosts:
            args = ['ping', host]
            result = subprocess.run(args, capture_output=True, text=True)
            return result.stdout
        else:
            raise ValueError('Host not allowed')
app = FastAPI()
@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    safe_ping_instance = SafePing()
    try:
        output = safe_ping_instance.safe_ping(host)
        return {"status": "completed", "output": output}
    except ValueError as e:
        return {"status": "error", "message": str(e)}