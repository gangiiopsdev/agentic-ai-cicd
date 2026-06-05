from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def safe_ping(host: str):
        # Validate and sanitize the host parameter
        if not host.isalnum():
            raise ValueError('Invalid hostname')
        
        # Use shlex.split to safely handle the command arguments
        cmd = ['ping', host]
        args = shlex.split(' '.join(cmd))
        subprocess.run(args, check=True)
class PingRouter:
    app = FastAPI()
    @staticmethod
    def ping(host: str):
        return SafePing.safe_ping(host)