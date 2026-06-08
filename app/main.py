from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.ping_command = ['ping']

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    result = safe_ping_instance.safe_ping(host)
    return {'status': 'completed', 'result': result}

def safe_ping(self, host: str):
    try:
        command = self.ping_command + shlex.split(host)
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, timeout=5)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.output.decode('utf-8')