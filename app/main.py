from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self):
        self.command = ['ping', 'google.com']  # Example command, replace with actual host

    async def ping(self):
        try:
            output = subprocess.check_output(shlex.split(' '.join(self.command)), stderr=subprocess.STDOUT)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'error': e.output.decode('utf-8')}

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping():
    return safe_ping_instance.ping()