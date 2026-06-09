from fastapi import FastAPI
import subprocess
import shlex
def is_safe_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of safe hosts
    return host in allowed_hosts
class PingCommand:
    def __init__(self, command):
        self.command = command
    def execute(self):
        subprocess.run(self.command, check=True)
def get_ping_command(host):
    if is_safe_host(host):
        return PingCommand(['ping', shlex.quote(host)])
    else:
        raise ValueError("Unauthorized host")
app = FastAPI()
@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get(")
def ping(host: str):
    try:
        command = get_ping_command(host)
        command.execute()
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e)}, 403