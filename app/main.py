from fastapi import FastAPI
import subprocess
class Ping:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        # Safe implementation
        args = ['ping', self.host]
        subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_instance = Ping(host)
    ping_instance.execute()
    return {"status": "completed"}