from fastapi import FastAPI
import subprocess
class SubprocessExecutor:
    @staticmethod
def safe_ping(host: str):
        if not host.isalnum():
            raise ValueError('Invalid host')
        return ['ping', host]

global executor = SubprocessExecutor()

app = FastAPI()

def ping(host: str):
    command = executor.safe_ping(host)
    try:
        output = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)