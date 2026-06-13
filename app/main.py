from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run(command, **kwargs):
        args = shlex.split(command)
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
class PingRouter:
    def __init__(self, app: FastAPI):
        self.app = app
        app.add_api_route('/ping', self.ping)

    async def ping(self, host: str):
        try:
            output = SafeSubprocess.run('ping ' + shlex.quote(host))
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}
class HomeRouter:
    def __init__(self, app: FastAPI):
        self.app = app
        app.add_api_route('/', self.home)

    async def home(self):
        return {'message': 'Agentic Self-Healing Pipeline'}
def setup_app():
    app = FastAPI()
    HomeRouter(app)
    PingRouter(app)
    return app