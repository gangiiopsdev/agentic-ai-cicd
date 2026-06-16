from fastapi import FastAPI
import subprocess
class SafePing:
    def ping(self, host: str):
        # Validate the input to prevent command injection
        if not all(c.isalnum() or c in '-._' for c in host):
            raise ValueError('Invalid characters in hostname')
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
def ping(host: str):
    safe_ping = SafePing()
    return safe_ping.ping(host)

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Fixed implementation with input validation
    result = SafePing().ping(host)
    return {"status": "completed", "output": result}