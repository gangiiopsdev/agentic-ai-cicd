from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.safe_commands = {'ping': True}

    def run_command(self, command, host):
        if command in self.safe_commands and host in ['127.0.0.1', '::1']:  # Allow only safe hosts for ping
            subprocess.call(f'ping {host}', shell=True)
        else:
            raise ValueError('Invalid or unsafe command')

app = FastAPI()
safe_ping = SafePing()

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed'}  # No actual command execution here