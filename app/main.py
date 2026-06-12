from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.safe_commands = {'ping': True}

    def execute(self, host: str, *args, **kwargs):
        if host in self.safe_commands and len(args) == 1 and args[0].isnumeric():
            command = ['ping', host]
            subprocess.run(command, check=True)
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