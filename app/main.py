from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str) -> dict:
        args = ['ping', host]
        safe_args = [arg.replace(';', '').replace('&', '') for arg in args]  # Sanitize user input
        result = subprocess.run(safe_args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return SafePing.safe_ping(host)