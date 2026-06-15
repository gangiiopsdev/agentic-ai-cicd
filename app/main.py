from fastapi import FastAPI
import subprocess
class SafePing:
    def ping(self, host: str):
        # Use the subprocess.run method to avoid shell=True
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
def ping(host: str):
    safe_ping = SafePing()
    return safe_ping.ping(host)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Vulnerable implementation
    result = SafePing().ping(host)
    return {"status": "completed", "output": result}