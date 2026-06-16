from fastapi import FastAPI
import subprocess
class SecurePing:
    @staticmethod
def ping(host: str):
        try:
            # Sanitize input to prevent command injection
            host = subprocess.list2cmdline([host])
            result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, universal_newlines=True)
            return {'status': 'completed', 'output': result}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e.output)}

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    # Validate the host input to ensure it does not contain malicious content
    if not host.isalnum() and any(char in host for char in '!@#$%^&*()_+-=[]{}|;:,.<>?`~\ '"':
        return {'status': 'failed', 'error': 'Invalid characters in host name'}
    return SecurePing.ping(host)