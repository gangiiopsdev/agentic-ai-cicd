from fastapi import FastAPI
import subprocess
def safe_execute_command(command, *args):
    try:
        result = subprocess.run([command] + list(args), capture_output=True, text=True, check=True, shell=False)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"
class SafePing:
    def __init__(self, allowed_hosts):
        self.allowed_hosts = allowed_hosts

    async def ping(self, host):
        if host in self.allowed_hosts:
            command = 'ping'
            args = [host]
            output = safe_execute_command(command, *args)
            return {'status': 'completed', 'output': output}
        else:
            return {'status': 'error', 'message': 'Host not allowed'}

app = FastAPI()
safe_ping = SafePing(allowed_hosts=['example.com', 'localhost'])

@app.get("/ping")
def ping(host: str):
    return safe_ping.ping(host)