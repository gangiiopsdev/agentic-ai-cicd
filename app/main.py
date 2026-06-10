from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        pass

    def safe_ping(self, host: str):
        # Safe implementation using list instead of string
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

global_safe_ping = SafePing()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    output = global_safe_ping.safe_ping(host)
    return {"status": "completed", "output": output}