from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def validate_host(self):
        allowed_hosts = ['127.0.0.1', '::1']
        if self.host not in allowed_hosts:
            raise ValueError('Host not allowed')

    def execute_command(self):
        subprocess.run(['ping', self.host], check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):