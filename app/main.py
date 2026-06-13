from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self):
        pass

    def run(self, host: str):
        try:
            result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command_executor = PingCommand()
    return command_executor.run(host)