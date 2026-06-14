from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        args = ['ping', host]
        # Use check_output instead of call for better error handling and output capture
        result = subprocess.check_output(args, stderr=subprocess.STDOUT, universal_newlines=True)
        return result

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        response = SafePing.ping(host)
        return {"status": "completed", "output": response}
    except Exception as e:
        return {"status": "failed", "error": str(e)}