from fastapi import FastAPI
import subprocess
from shlex import quote

class CommandEscaper:
    def __init__(self):
        self.safe_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'

    def escape(self, string):
        return ''.join(c for c in string if c in self.safe_chars)

escaper = CommandEscaper()

def escape_command(command):
    return [quote(arg) for arg in command]

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    escaped_host = escaper.escape(host)
    result = subprocess.run(['ping', '-c 1', escaped_host], capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout}