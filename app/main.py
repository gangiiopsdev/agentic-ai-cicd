from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        try:
            result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    if not all(c.isalnum() or c in '._' for c in host):
        raise ValueError('Invalid input')
    output = SafePing.safe_ping(subprocess.list2cmdline([host]))
    return {"status": "completed", "output": output}