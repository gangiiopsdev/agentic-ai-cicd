from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.ping_command = 'ping'

    def ping(self, host: str):
        # Safe implementation using subprocess.call with shell=False
        try:
            result = subprocess.run([self.ping_command, host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return str(e.stderr.decode('utf-8'))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing()
    return {"status": "completed", "output": safe_ping.ping(host)}