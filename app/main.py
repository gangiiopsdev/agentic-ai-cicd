from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def safe_ping(host: str) -> bool:
        allowed_hosts = ['google.com', 'example.com']
        if host not in allowed_hosts:
            return False
        try:
            result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(e.stderr)
            return False

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if PingCommand.safe_ping(host):
        return {"status": "completed", "host": host}
    else:
        return {"status": "failed", "host": host}