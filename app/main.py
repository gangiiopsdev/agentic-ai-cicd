from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
    def ping(host: str):
        # Using check_output instead of call to capture the output safely
        result = subprocess.check_output(['ping'] + shlex.split(host), stderr=subprocess.STDOUT, universal_newlines=True)
        return {'status': 'completed', 'output': result}
global app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    # Sanitize the input to prevent command injection
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host')
    return SafeSubprocess.ping(host)