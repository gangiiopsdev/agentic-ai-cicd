from fastapi import FastAPI
import re
import shlex
class HostValidator:
    ALLOWED_HOSTS = {'example.com', 'test.com'}

    @staticmethod
def is_valid_host(host):
        return host in HostValidator.ALLOWED_HOSTS

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not HostValidator.is_valid_host(host) or re.match(r'^[a-zA-Z0-9.-]+$', host) is None:
        return {'status': 'error', 'output': 'Invalid input'}
    result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}