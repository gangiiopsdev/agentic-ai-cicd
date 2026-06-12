from fastapi import FastAPI
import subprocess
import shlex
def safe_ping_command(host: str) -> str:
    return f'ping -c 1 {host}'

class SafePing:
    def __init__(self):
        self.ping_command = 'ping'

    async def safe_ping(self, host: str):
        try:
            result = subprocess.run(shlex.split(f'{self.ping_command} {safe_ping_command(host)}'), capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    return safe_ping_instance.safe_ping(host)