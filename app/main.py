from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def sanitize_input(host):
        # Basic sanitization, real-world use should be more robust
        return ''.join(filter(str.isalnum, host))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = PingCommand.sanitize_input(host)
    subprocess.call(f"ping {sanitized_host}", shell=False)
    return {"status": "completed"}