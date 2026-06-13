from fastapi import FastAPI
import subprocess
import shlex
def execute_ping(host):
    try:
        # Use os.path.join to ensure the full path of the executable is used
        result = subprocess.run(['ping', *shlex.split(host)], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

class App:
    def __init__(self):
        self.app = FastAPI()

    @app.get('/')
    def home(self):
        return {'message': 'Agentic Self-Healing Pipeline'}

    @app.get('/ping')
    def ping(self, host: str):
        # Validate host input
        if not self.is_valid_host(host):
            return {'status': 'error', 'result': 'Invalid host input'}
        result = execute_ping(host)
        return {'status': 'completed', 'result': result}

    def is_valid_host(self, host: str) -> bool:
        # Basic validation for alphanumeric and length
        return host.isalnum() and len(host) <= 64

app_instance = App()