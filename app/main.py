from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def safe_ping(host):
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=False)
            return output.stdout or output.stderr
        except Exception as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'result': 'Invalid host'}
    result = SafeSubprocess.safe_ping(host)
    return {'status': 'completed', 'result': result}