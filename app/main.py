from fastapi import FastAPI
import subprocess
import shlex

class SafeCommandRunner:
    def __init__(self):
        self.safe_commands = ['ping']

    def run(self, command: str, *args, **kwargs):
        if not any(command.startswith(safe_command) for safe_command in self.safe_commands):
            raise ValueError('Unsafe command detected')
        subprocess.run([command] + list(args), check=True, capture_output=True, text=True)

app = FastAPI()
safe_runner = SafeCommandRunner()

@app.get("/ping")
def ping(host: str):
    return safe_runner.run('ping', host)