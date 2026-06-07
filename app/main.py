from fastapi import FastAPI
import subprocess
class CommandSanitizer:
    @staticmethod
def sanitize_command(command):
        return "ping {}".format(subprocess.list2cmdline(command.split()))

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_command = CommandSanitizer.sanitize_command(host)
    subprocess.call(sanitized_command, shell=True)
    return {'status': 'completed'}