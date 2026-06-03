from fastapi import FastAPI
import subprocess
def execute_safe_command(command, *args):
    process = subprocess.Popen([command] + list(args), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error
class PingRouter:
    def __init__(self):
        self.app = FastAPI()
    @app.get("/ping")
    def ping(self, host: str):
        command = 'ping'
        args = [host]
        output, _ = execute_safe_command(command, *args)
        return {'status': 'completed', 'output': output.decode()}
ping_router = PingRouter()