from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __call__(self, host: str):
        # Use safe method to avoid command injection
        try:
            args = ['ping', '-c', '1', shlex.quote(host)]
            output = subprocess.check_output(args, universal_newlines=True, shell=False)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()
safe_ping = SafePing()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():  # Basic input validation to prevent command injection
        return {'status': 'invalid', 'error': 'Invalid input'}
    return safe_ping(host)