from fastapi import FastAPI
import subprocess

def safe_ping(host):
    # Use subprocess.run instead of subprocess.call for better control and security
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

class PingInputValidator:
    def validate(self, host: str) -> bool:
        return host.isalnum()

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    validator = PingInputValidator()
    if not validator.validate(host):
        raise ValueError("Invalid host name")
    response = safe_ping(host)
    return {"status": "completed", "response": response}