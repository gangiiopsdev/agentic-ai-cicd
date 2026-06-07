from fastapi import FastAPI
import shlex
class SafePing:
    def __call__(self, host: str):
        cmd = ['ping', '-c', '1', host]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.returncode == 0, result.stdout,

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing()
    status, output = safe_ping(host)
    return {"status": status, "output": output}