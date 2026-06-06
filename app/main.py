from fastapi import FastAPI
import subprocess
class SafePinger:
    @staticmethod
def ping(host: str):
        # Validate the host input to ensure it is safe
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid host name')
        try:
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    pinger = SafePinger()
    return pinger.ping(host)