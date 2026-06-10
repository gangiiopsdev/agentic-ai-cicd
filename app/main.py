from fastapi import FastAPI
import subprocess
import shlex

class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def run(self) -> dict:
        command = ['ping', shlex.quote(self.host)]
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return PingCommand(host).run()