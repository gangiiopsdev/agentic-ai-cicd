from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            args = ['ping', '-c', '1'] + [shlex.quote(arg) for arg in shlex.split(self.host)]
            output = subprocess.check_output(args, stderr=subprocess.STDOUT)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode('utf-8')}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    return command.execute()