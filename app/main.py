from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run_command(command: str, *args, **kwargs):
        try:
            cmd = shlex.split(command)
            result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, *args, **kwargs)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr}"
class PingRouter:
    def __init__(self):
        self.app = FastAPI()

    @app.get("/ping")
    def ping(self, host: str):
        # SafeSubprocess.run_command should not be used with user input for command construction
        result = SafeSubprocess.run_command(f'ping {host}', shell=False)
        return {'status': 'completed', 'result': result}
ping_router = PingRouter()