from fastapi import FastAPI
import subprocess
class SafePing:
    def ping(self, host: str):
        # Safe implementation using subprocess.run
        args = ['ping', host]
        subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_pinger = SafePing()
    safe_pinger.ping(host)
    return {"status": "completed"}