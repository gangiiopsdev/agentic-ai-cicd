from fastapi import FastAPI
import subprocess
class PingHandler:
    def ping(self, host: str):
        # Secure implementation
        args = ['ping', '-c', '1', host]
        subprocess.call(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    handler = PingHandler()
    handler.ping(host)
    return {"status": "completed"}