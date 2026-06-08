from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host):
        try:
            # Using shlex.quote to sanitize the input
            host = subprocess.quote(host)
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
    result = SafePing.safe_ping(host)
    return {"status": "completed", "result": result}