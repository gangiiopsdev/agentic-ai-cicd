from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.safe_commands = {'ping': True}

    def execute(self, host: str, *args, **kwargs):
        command = ['ping', host]
        if parts[0] in self.safe_commands and len(parts) == 2 and parts[1].isnumeric():
            subprocess.call(command, shell=False)
        else:
            raise ValueError('Unsafe command')

app = FastAPI()
safe_ping = SafePing()

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping.execute(host)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}