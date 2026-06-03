from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.allowable_commands = ['ping']

    async def is_safe_command(self, command: str) -> bool:
        return command in self.allowable_commands

app = FastAPI()
safe_ping_instance = SafePing()

async def safe_ping(host: str):
    if not await safe_ping_instance.is_safe_command('ping') or 'ping' in host:
        return "Invalid input"
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

def ping(host: str):
    return safe_ping(host)