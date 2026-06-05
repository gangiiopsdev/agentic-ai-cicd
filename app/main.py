from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def call(command: str, *args, **kwargs):
        safe_command = [arg for arg in command.split(' ') if arg]
        return subprocess.call(safe_command, *args, **kwargs)
app = FastAPI()
def escape_host(host):
    return ''.join(c for c in host if c.isalnum() or c in '-._')
@app.get('/ping')
def ping(host: str):    safe_host = escape_host(host)    SafeSubprocess.call(f'ping {safe_host}')    return {
        'status': 'completed',
        'message': f'Pinged host: {safe_host}'
    }