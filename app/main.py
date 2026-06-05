from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        if not host.isalnum():
            return {"status": "failed", "error": "Invalid input"}
        output, error = subprocess.run(['ping', host], capture_output=True, text=True)
        return {"status": "completed", "output": output, "error": error}
    except Exception as e:
        return {"status": "failed", "error": str(e)}