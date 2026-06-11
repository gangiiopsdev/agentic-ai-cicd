from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    @staticmethod
def ping(host: str):
        cmd = ['ping', host]
        args = shlex.split(' '.join(cmd))
        try:
            result = subprocess.run(args, check=True, shell=False)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    if not PingService.is_valid_host(host):
        raise ValueError("Invalid host")
    return PingService.ping(host)
class PingService:
    @staticmethod
def is_valid_host(host: str) -> bool:
        # Add validation logic here, e.g., check for IP address format or domain name validity
        import re
        pattern = r'^([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}|[a-zA-Z0-9.-]+)$'
        return bool(re.match(pattern, host))