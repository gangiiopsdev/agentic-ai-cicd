from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    @staticmethod
def ping(host: str):
        if not validate_host(host):
            return {"status": "error", "output": "Invalid hostname"}
        try:
            args = ['ping', '-c', '1'] + [arg for arg in shlex.split(host) if isinstance(arg, str)]
            output = subprocess.run(args, capture_output=True, text=True, check=False)
            if output.returncode == 0:
                return {"status": "completed", "output": output.stdout}
            else:
                return {"status": "error", "output": output.stderr}
        except Exception as e:
            return {"status": "error", "output": str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return PingService.ping(host)
def validate_host(host):  # Simple regex for basic hostname validation
    import re
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None