from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.safe_hosts = ['localhost', '127.0.0.1']  # Define a list of allowed hosts

    def is_safe_host(self, host):
        return host in self.safe_hosts

    async def ping(self, host: str):
        if not self.is_safe_host(host):
            raise ValueError('Invalid host')
        args = shlex.split(f'ping {host}')
        result = await asyncio.create_subprocess_exec(*args,
                                             stdin=subprocess.DEVNULL,
                                             stdout=subprocess.PIPE,
                                             stderr=subprocess.PIPE)
        output, error = await result.communicate()
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, args, output, error)
        return {'status': 'completed'}

app = FastAPI()
ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    return ping_instance.ping(host)