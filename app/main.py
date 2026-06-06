from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_safe(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'error': 'Invalid host'}
    return SafeSubprocess.ping(host)

def is_valid_host(host: str) -> bool:
    # Simple check to ensure the host does not contain potentially harmful characters
    return all(c.isalnum() or c in ('.', '-') for c in host)