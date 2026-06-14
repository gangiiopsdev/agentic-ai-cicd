from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    @staticmethod
def ping(host: str):
        if not validate_host(host):
            return {"status": "error", "output": "Invalid hostname"}
        try:
            args = ['ping', '-c', '1'] + [shlex.quote(part) for part in host.split()]
            output = subprocess.check_output(args, stderr=subprocess.STDOUT, universal_newlines=True, shell=False)
            return {"status": "completed", "output": output}
        except subprocess.CalledProcessError as e:
            return {"status": "error", "output": e.output}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return PingService.ping(host)
def validate_host(host):  # Simple regex for basic hostname validation
    import re
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None