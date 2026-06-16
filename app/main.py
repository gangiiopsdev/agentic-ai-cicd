from fastapi import FastAPI
import subprocess
import shlex
class HostValidator:
    def is_valid(self, host: str) -> bool:
        return not host.isdigit() and '@' not in host

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    validator = HostValidator()
    if validator.is_valid(host):
        command = ['ping', host]
        subprocess.run(command, check=True)
        return {"status": "completed"}
    else:
        return {"status": "invalid_host"}