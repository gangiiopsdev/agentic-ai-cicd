from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    @staticmethod
def safe_ping(host: str):
        # Validate and sanitize input
        if not host or not host.strip():
            raise ValueError('Invalid host provided')
        args = ['ping', '-c', '1', shlex.quote(host)]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    output = SafePing.safe_ping(host)
    return {"status": "completed", "output": output}