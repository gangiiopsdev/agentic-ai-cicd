from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def safe_run(command: str, *args, **kwargs):
        try:
            result = subprocess.run([command] + list(shlex.split(' '.join(args))), capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)
class PingRouter:
    @staticmethod
def ping(host: str):
        # Sanitize input to prevent command injection
        if not host.isalnum() or ' ' in host:
            return {'status': 'error', 'output': 'Invalid input'}
        output = SafeSubprocess.safe_run('ping', shlex.quote(host))
        return {'status': 'completed', 'output': output}app = FastAPI()

app.get("/ping")(PingRouter.ping)