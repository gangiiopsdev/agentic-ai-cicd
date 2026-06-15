from fastapi import FastAPI
import subprocess
class SafePing:
    def ping(self, host: str):
        if not self.is_safe_host(host):
            raise ValueError('Unsafe host')
        subprocess.call(['ping', host])

    def is_safe_host(self, host: str) -> bool:
        safe_hosts = ['127.0.0.1', '::1']  # Example list of safe hosts
        return host in safe_hosts

global_ping = SafePing()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global_ping.ping(host)
    return {"status": "completed"}