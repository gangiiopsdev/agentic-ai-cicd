from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def safe_ping(host):
        if not host or ' ' in host:
            return "Invalid host"
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True)
            return output.stdout
        except Exception as e:
            return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = SafeSubprocess.safe_ping(host)
    return {"status": "completed", "result": result}