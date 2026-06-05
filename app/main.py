from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host):
        self.host = host.strip()

    def is_safe(self):
        return not any(char in self.host for char in ' \t\u000b\r\f\v`|&*;{}[]<>,.?/~^%$#@!')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_host = PingCommand(host)
    if safe_host.is_safe():
        subprocess.call(['ping', shlex.quote(safe_host.host)])
    return {"status": "completed"}