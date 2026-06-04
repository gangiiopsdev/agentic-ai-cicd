from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.ping_command = ['ping', 'localhost']  # Replace 'localhost' with a valid target

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not SafePing().is_safe_target(host):
        raise Exception("Invalid target for ping")
    subprocess.call(SafePing().ping_command)
    return {"status": "completed"}
class SafePing:
    def __init__(self):
        self.ping_command = ['ping', 'localhost']  # Replace 'localhost' with a valid target

    def is_safe_target(self, host):
        safe_targets = ['localhost', '127.0.0.1']  # Define a list of safe targets
        return host in safe_targets