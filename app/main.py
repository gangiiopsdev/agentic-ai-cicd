from fastapi import FastAPI
import subprocess
class SafePing:
    def __call__(self, host):
        if not self.is_safe(host):
            raise ValueError('Unsafe host name detected')
        subprocess.call(['ping', host])

    def is_safe(self, host):
        return all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in host)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing()
    safe_ping(host)
    return {"status": "completed"}