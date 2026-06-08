from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self):
        pass

    def execute(self, host: str):
        try:
            result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return PingCommand().execute(host)