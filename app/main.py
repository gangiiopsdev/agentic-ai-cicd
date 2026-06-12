from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self):
        self.allowed_commands = ['ping']

    async def safe_ping(self, host):
        if 'ping' not in self.allowed_commands or '&&' in host or '|' in host or ';' in host:
            return {'error': 'Invalid input'}, 400
        try:
            args = shlex.split(f'ping {host}')
            result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = await result.communicate()
            if result.returncode != 0:
                return {'error': stderr.decode('utf-8')}, 500
            return stdout.decode('utf-8'), 200
        except Exception as e:
            return str(e), 500

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    return safe_ping_instance.safe_ping(host)