from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Secure implementation using subprocess.run with shell=False and ensuring input is sanitized
        try:
            result = subprocess.run(['ping', self.host], check=True, capture_output=True, text=True, shell=False)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if '||' in host or '&' in host or ';' in host:
        return {'status': 'failed', 'error': 'Invalid characters detected in host parameter'}
    return PingCommand(host).execute()