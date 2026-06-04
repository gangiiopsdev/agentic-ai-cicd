from fastapi import FastAPI
import subprocess
import shlex
def execute_ping(host):
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
class App:
    def __init__(self):
        self.app = FastAPI()

    @app.get("/ping")
    def ping(self, host: str):
        response = execute_ping(host)
        return {"status": "completed", "output": response}
App().app