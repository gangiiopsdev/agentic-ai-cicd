from fastapi import FastAPI
import re

class PingCommand:
    def __init__(self, host: str):
        self.host = host

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        if not re.match(r'^[a-zA-Z0-9]+$', host):
            return {"status": "failed", "error": "Invalid input"}
        process = PingCommand(host)
        output, error = process.communicate()
        return {"status": "completed", "output": output.decode(), "error": error.decode()}
    except Exception as e:
        return {"status": "failed", "error": str(e)}