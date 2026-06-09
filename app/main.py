from fastapi import FastAPI
import subprocess
class SafeCommandRunner:
    def run(self, command, *args):
        if isinstance(command, list) and command[0] == 'ping':
            return subprocess.call(command + args)
        else:
            raise ValueError('Unsafe command')

app = FastAPI()
safe_runner = SafeCommandRunner()

@app.get("/ping")
def ping(host: str):
    return safe_runner.run(['ping'], host)