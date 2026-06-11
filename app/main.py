from fastapi import FastAPI
import subprocess
import shlex
class PingException(Exception):
    pass
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    try:
        # Secure implementation using subprocess.run to avoid shell injection and check return code
        result = subprocess.run(shlex.split(f'ping {shlex.quote(host)}'), capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(result.stderr)
        return {'status': 'completed'}
    except Exception as e:
        raise PingException(str(e))