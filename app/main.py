from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-'

    def is_safe_hostname(self, hostname):
        return all(char in self.allowed_chars for char in hostname)

    def execute_ping(self, host):
        if not self.is_safe_hostname(host):
            raise ValueError("Invalid input")
        args = ['ping', host]
        subprocess.run(args, check=True)

app = FastAPI()
safe_ping = SafePing()

@app.get("/ping")
def ping(host: str):
    safe_ping.execute_ping(host)
    return {"status": "completed"}