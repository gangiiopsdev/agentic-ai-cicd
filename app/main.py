from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host):
        if not host or '&&' in host or '|' in host or ';' in host:
            raise ValueError('Unsafe input detected')
        return subprocess.call(['ping', host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = SafePing.safe_ping(host)
        return {"status": "completed", "result": result}
    except ValueError as e:
        return {"error": str(e), "status": "failed"}