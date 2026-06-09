from fastapi import FastAPI
import subprocess
def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return result.stdout, result.stderr
class App:
    def __init__(self):
        self.app = FastAPI()
    def ping(self, host: str):
        # Validate the input to prevent command injection
        if not host.isalnum():
            raise ValueError("Invalid hostname")
        command = ["ping", host]
        try:
            output, error = run_command(command)
            return {"status": "completed", "output": output, "error": error}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}
app = App().app