from fastapi import FastAPI
import subprocess
import shlex

class SafeCommand:
    def __init__(self, *args):
        self.args = args

    def run(self):
        try:
            result = subprocess.run(self.args, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'output': e.stderr}
        except Exception as e:
            return {'status': 'error', 'output': str(e)}

app = FastAPI()

@app.get('/ping/{host}')
def ping(host: str):
    if not host.isalnum():  # Simple validation to avoid command injection
        return {'status': 'error', 'output': 'Invalid input'}
    safe_command = SafeCommand('ping', host)
    return safe_command.run()