from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safer implementation using subprocess.run with shell=False and validation
        if not self._is_valid_host(self.host):
            raise ValueError('Invalid host')
        args = ['ping', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

    @staticmethod
    def _is_valid_host(host: str) -> bool:
        # Simple regex to validate the host format
        import re
        pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
        return bool(pattern.match(host))
class PingEndpoint:
    def __init__(self):
        pass

    @staticmethod
    def ping(host: str):
        command = PingCommand(host)
        return {'status': 'completed', 'result': command.execute()}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    endpoint = PingEndpoint()
    return endpoint.ping(host)