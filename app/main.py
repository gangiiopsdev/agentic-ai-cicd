from fastapi import FastAPI
import subprocess
def run_command(command):
    # Validate and sanitize the command input here
    safe_command = ['ping', command]
    result = subprocess.run(safe_command, capture_output=True, text=True, shell=False)
    return result.stdout, result.stderr
class App:
    def __init__(self):
        self.app = FastAPI()
    def ping(self, host: str):
        output, error = run_command(host)
        return {"status": "completed", "output": output, "error": error}app = App().app