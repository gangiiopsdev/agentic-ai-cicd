from fastapi import FastAPI
import subprocess
import shlex
class PingRequest:
    def __init__(self, host: str):
        self.host = host

    def validate(self) -> bool:
        return self.host.isalnum()

    def execute(self) -> dict:
        if not self.validate():
            return {'status': 'failed', 'error': 'Invalid host input'}
        command = ['ping'] + shlex.split(self.host)
        try:
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode()}
        except subprocess.TimeoutExpired:
            return {'status': 'timeout', 'message': 'Ping request timed out'}
class PingRouter:
    @staticmethod
    async def ping(host: str):
        return PingRequest(host).execute()
app = FastAPI()
app.add_api_route('/ping', PingRouter.ping, methods=['GET'])