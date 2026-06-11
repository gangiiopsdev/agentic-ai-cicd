from fastapi import FastAPI
import subprocess
import re
class SafePing:
    @staticmethod
def ping(host: str):
        # Validate and sanitize the host input to prevent injection attacks
        try:
            if not re.match(r'^[a-zA-Z0-9.-]+$', host):
                return 'Invalid host'
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return output.stdout
        except (subprocess.CalledProcessError, re.error) as e:
            return f'Error pinging {host}: {str(e)}'

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_wrapper(host: str):
    # Sanitize the input before passing it to subprocess.run
    sanitized_host = re.sub(r'[^a-zA-Z0-9.-]', '', host)
    result = SafePing.ping(sanitized_host)
    return {'status': 'completed', 'result': result}