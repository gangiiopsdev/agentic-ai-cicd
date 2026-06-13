from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    @staticmethod
def run(host: str):
        if not host.isnumeric():
            raise ValueError('Invalid input')
        args = ['ping', '-c', '1', '--', shlex.quote(host)]  # Add -- before the quoted argument to prevent command injection
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

global _ping_command_cache {}

def get_ping_command_instance():
    global _ping_command_cache
    if '_ping_command_cache' not in globals() or _ping_command_cache is None:
        _ping_command_cache = PingCommand()
    return _ping_command_cache

app = FastAPI()

@app.get('/ping')
def ping_endpoint(host: str):
    try:
        return get_ping_command_instance().run(host)
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}