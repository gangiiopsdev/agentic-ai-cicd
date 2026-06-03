from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation using subprocess.run()
        args = ['ping', '-c', '1', self.host]
        result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode(), result.stderr.decode()

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    command = PingCommand(host)
    stdout, stderr = command.execute()
    if stderr:
        return {"status": "failed", "error": stderr.decode()}
    else:
        return {"status": "completed", "stdout": stdout.decode()}