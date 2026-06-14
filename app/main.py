from fastapi import FastAPI
import re
from subprocess import Popen, PIPE, CalledProcessError

def validate_host(host: str) -> bool:
    # Enhanced regex to validate a host more thoroughly
    return re.match(r'^[a-zA-Z0-9.-]{1,253}$', host) is not None

def safe_ping(host: str):
    args = ['ping', '-c', '4', host]
    if not validate_host(host):
        raise ValueError("Invalid host")
    try:
        process = Popen(args, stdout=PIPE, stderr=PIPE)
        output, error = process.communicate()
        if process.returncode != 0:
            return str(error.decode('utf-8'))
        else:
            return output.decode('utf-8')
    except Exception as e:
        return str(e)

class PingService:
    def ping(self, host: str) -> dict:
        try:
            output = safe_ping(host)
            return {"status": "completed", "output": output}
        except ValueError as e:
            return {"status": "error", "message": str(e)}

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    return ping_service.ping(host)