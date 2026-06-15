from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self):
        self.app = FastAPI()

    async def ping(self, host: str):
        try:
            if not self.is_valid_host(host):
                raise ValueError("Invalid host")
            args = shlex.split(f"ping {host}")
            result = subprocess.run(args, check=True, capture_output=True, text=True)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "error", "message": str(e)}

    def is_valid_host(self, host: str) -> bool:
        # Add logic to validate the host input
        allowed_hosts = ['192.168.1.1', '10.0.0.1']  # Example list of allowed hosts
        return host in allowed_hosts
ping_command = PingCommand()