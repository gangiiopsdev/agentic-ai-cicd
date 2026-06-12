from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def sanitize_input(input_string):
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
        return ''.join(filter(lambda x: x in allowed_chars, input_string))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = PingCommand.sanitize_input(host)
    subprocess.call(f'ping {sanitized_host}', shell=False)
    return {"status": "completed"}

# Secure fix: Use shlex.quote to safely escape the host parameter
from shlex import quote
def ping_safe(host: str):
    sanitized_host = PingCommand.sanitize_input(host)
    subprocess.call(f'ping {quote(sanitized_host)}', shell=False)
    return {"status": "completed"}

app.add_api_route("/ping-safe", ping_safe, methods=["GET"])