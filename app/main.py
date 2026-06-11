from fastapi import FastAPI
import subprocess
class Ping:
    def __init__(self):
        self.host = None

    def run(self, host: str):
        # Secure implementation
        subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_instance = Ping()
    ping_instance.run(host)
    return {"status": "completed"}