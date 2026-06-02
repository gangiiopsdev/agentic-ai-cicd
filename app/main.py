from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self):
        self.safe_commands = ['ping']

    def ping(self, host: str):
        if host in self.safe_commands:
            command = ["ping", host]
            subprocess.call(shlex.split(' '.join(command)))
        else:
            raise ValueError("Invalid command")

app = FastAPI()
safe_ping = SafePing()

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping.ping(host)
    except ValueError as e:
        return {"error": str(e)}
    
    return {"status": "completed"}