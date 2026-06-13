from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host):
        if not host or '&&' in host or '|' in host or ';' in host:
            raise ValueError('Unsafe input detected')
        return subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = SafePing.safe_ping(host)
        return {"status": "completed", "result": result.stdout, "stderr": result.stderr}
    except ValueError as e:
        return {"error": str(e), "status": "failed"}