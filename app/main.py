from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    # Sanitize input by escaping special characters or using a whitelist
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
class FastApiApp:
    def __init__(self):
        self.app = FastAPI()

    def ping(self, host: str):
        # Sanitize input by validating against a whitelist
        if host not in ['127.0.0.1', 'localhost']:
            return {'status': 'error', 'message': 'Invalid host'}
        output = run_ping(host)
        return {'status': 'completed', 'output': output}
class AppInstance(FastApiApp):
    def __init__(self):
        super().__init__()
        self.app.get('/ping')(self.ping)

app_instance = AppInstance().app