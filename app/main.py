from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self):
        self.safe_commands = ['ping']

    async def _check_command(self, command: str) -> bool:
        return any(command.startswith(safe_command) for safe_command in self.safe_commands)

    async def execute(self, host: str) -> bool:
        if not await self._check_command(host):
            raise ValueError('Unsafe command detected')
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        if safe_ping_instance.execute(host):
            return {"status": "completed", "output": 'Ping successful'}
    except ValueError as e:
        return {"status": "failed", "error": str(e)}