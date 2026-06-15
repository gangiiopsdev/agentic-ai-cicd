from fastapi import FastAPI
import subprocess
import re
def run_ping(host):
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
class HostValidator:
    @staticmethod
def validate_host(host: str) -> bool:
        pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
        if not pattern.match(host):
            return False
        return True
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if HostValidator.validate_host(host):
        output = run_ping(host)
        return {"status": "completed", "output": output}
    else:
        return {"error": "Invalid host parameter"}