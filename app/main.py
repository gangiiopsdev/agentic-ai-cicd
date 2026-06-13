from fastapi import FastAPI
import subprocess

app = FastAPI()

class PingCommand(subprocess.Popen):
    def __init__(self, *args, **kwargs):
        if 'shell' in kwargs and kwargs['shell']:
            raise ValueError('Shell usage is not allowed for security reasons.')
        super().__init__(*args, **kwargs)

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')
    command = ['ping', host]
    PingCommand(command, shell=False)
    return {'status': 'completed'}