from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host):
        if not host.isalnum():
            raise ValueError('Invalid hostname')
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout,

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        output = SafePing.safe_ping(host)
        return {"status": "completed", "output": output}
    except ValueError as e:
        return {"error": str(e)}, 400