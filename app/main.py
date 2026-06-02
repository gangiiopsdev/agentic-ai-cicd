from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self):
        self.ping_command = ['ping']

    def run(self, host):
        full_command = self.ping_command + shlex.split(host)
        try:
            output = subprocess.run(full_command, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    return safe_ping_instance.run(host)