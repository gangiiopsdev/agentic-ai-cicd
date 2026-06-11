from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def safe_run(command, *args, **kwargs):
        if isinstance(command, str):
            command = shlex.split(command)
        return subprocess.run(command, *args, **kwargs)
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host or not isinstance(host, str) or len(host.strip()) == 0:
        return {'status': 'failed', 'output': 'Invalid host input'}
    result = SafeSubprocess.safe_run(['ping', shlex.quote(host)], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}