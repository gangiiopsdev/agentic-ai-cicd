from fastapi import FastAPI
import subprocess
class CommandEscaper:
    def __init__(self):
        self.safe_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'

    def escape(self, string):
        return ''.join(c for c in string if c in self.safe_chars)

global escaper
escaper = CommandEscaper()

def escape_command(command):
    return [escaper.escape(arg) for arg in command]

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    escaped_host = escaper.escape(host)
    subprocess.call(escape_command(['ping', escaped_host]))
    return {'status': 'completed'}