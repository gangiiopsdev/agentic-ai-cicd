from fastapi import FastAPI
import asyncio
import shlex
import subprocess

class SafePing:
    def __init__(self):
        self.allowed_hosts = ['example.com', 'test.com']

    async def safe_ping(self, host: str):
        if host in self.allowed_hosts:
            args = ['ping', '--icmp-type=echo', shlex.quote(host)]  # Use specific ping options for safety
            try:
                result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output, error = await result.communicate()
                if result.returncode != 0:
                    return {'status': 'failed', 'error': error.decode()}
                else:
                    return {'status': 'completed', 'output': output.decode()}
            except Exception as e:
                return {'status': 'failed', 'error': str(e)}
        else:
            return {'status': 'denied', 'message': 'Unauthorized host'}

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    # Ensure the input is within a whitelist of allowed hosts
    if host not in safe_ping_instance.allowed_hosts:
        return {'status': 'denied', 'message': 'Unauthorized host'}
    return safe_ping_instance.safe_ping(host)