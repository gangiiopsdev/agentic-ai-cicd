from fastapi import FastAPI
import subprocess
class SafePing:
    def __call__(self, host: str):
        if self.is_valid_host(host):
            return subprocess.call(['ping', host])
        else:
            raise ValueError('Invalid host')

    def is_valid_host(self, host: str) -> bool:
        # Add validation logic here to ensure the host is safe
        return True

app = FastAPI()

@app.get="/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    safe_ping = SafePing()
    result = safe_ping(host)
    return {"status": "completed", "result": result}