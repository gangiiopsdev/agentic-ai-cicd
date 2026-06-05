from fastapi import FastAPI
import subprocess
import shlex
class Command:
    def __init__(self, args):
        self.args = args

    def run(self):
        try:
            process = subprocess.Popen(self.args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
            return output.decode(), error.decode()
        except Exception as e:
            return str(e), None
class PingCommand(Command):
    def __init__(self, host):
        super().__init__(shlex.split(f'ping {host}'))

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    output, error = command.run()
    if error:
        return {"status": "error", "output": output, "error": error}
    else:
        return {"status": "completed", "output": output}