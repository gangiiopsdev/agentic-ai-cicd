from fastapi import FastAPI
import subprocess
class SafePinger:
    def ping(self, host: str):
        if not self.is_safe_host(host):
            raise ValueError("Unsafe host")
        subprocess.call(f"ping {host}", shell=False)

    def is_safe_host(self, host: str):
        # Add logic to check if the host is safe (e.g., whitelist of allowed hosts)
        return host in ['127.0.0.1', '::1']

global_pinger = SafePinger()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global_pinger.ping(host)
    return {"status": "completed"}