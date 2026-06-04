from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.allowed_hosts = {'127.0.0.1', '::1'}

    def safe_ping(self, host):
        if host not in self.allowed_hosts:
            raise ValueError("Host is not allowed")
        try:
            subprocess.call(['ping', '-c', '5', host], timeout=5)
            return True
        except Exception as e:
            print(e)
            return False

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping_instance.safe_ping(host)
        if result:
            return {"status": "completed", "result": "success"}
        else:
            return {"status": "failed", "result": "failure"}
    except ValueError as e:
        return {"error": str(e)}