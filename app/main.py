from fastapi import FastAPI
import subprocess
def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True, shell=False)
    return result.stdout, result.stderr
class App:
    def __init__(self):
        self.app = FastAPI()
    def ping(self, host: str):
        command = ["ping", host]
        output, error = run_command(command)
        return {"status": "completed", "output": output, "error": error}
app = App().app