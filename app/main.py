from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self, host):
        self.host = host

    def ping(self):
        try:
            command = ['ping', self.host]
            subprocess.run(command, check=True)
            return {"status": "completed"}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return SafePing(host).ping()