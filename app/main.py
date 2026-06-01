from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def safe_ping(host: str):
        if not host.isalnum():
            raise ValueError('Invalid host name')
        return subprocess.call(['ping', '-c', '1', host], capture_output=True, text=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):\n    result = PingCommand.safe_ping(host)\n    return {'status': 'completed', 'output': result}