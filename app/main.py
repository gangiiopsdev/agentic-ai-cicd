from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        if host.isnumeric() or (host.startswith('127.') and '.' in host) or host.startswith('::1'):
            return 'Invalid host'
        return subprocess.call(['ping', '-c', '4', host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_route(host: str):
    result = SafePing.ping(host)
    if isinstance(result, int) and result == 0:
        return {"status": "completed", "result": "Success"}
    else:
        return {"status": "failed", "result": "Failure"}