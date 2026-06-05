from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run(command, *args, **kwargs):
        if isinstance(command, str):
            command = shlex.split(command)
        return subprocess.run(command, *args, **kwargs)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        # Use a whitelist for allowed hosts to prevent command injection
        if host in ['allowed_host1', 'allowed_host2']:
            SafeSubprocess.run(['ping', '-c', '1', host], shell=False)
            return {'status': 'completed', 'result': 'success'}
        else:
            raise ValueError('Host not allowed')
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}