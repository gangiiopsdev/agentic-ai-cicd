from fastapi import FastAPI
import subprocess
class Ping:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Secure implementation using subprocess.Popen
        subprocess.run(['ping', self.host], check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_instance = Ping(host)
    ping_instance.execute()
    return {"status": "completed"}