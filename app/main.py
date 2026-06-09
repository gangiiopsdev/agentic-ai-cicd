from fastapi import FastAPI
import subprocess
from shlex import quote as escape_shell_arg
class PingService:
    def safe_execute(self, command: list):
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    safe_host = ' '.join([escape_shell_arg(arg) for arg in host.split()])
    command = ['ping', safe_host]
    return {'status': 'completed', 'output': ping_service.safe_execute(command)}