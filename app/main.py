from fastapi import FastAPI
import subprocess
def execute_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error
class PingRouter:
    def __init__(self):
        pass
    async def ping(self, host: str):
        command = ['ping', host]
        output, _ = execute_command(command)
        return {'status': 'completed', 'output': output.decode()}
app = FastAPI()
ping_router = PingRouter()
app.add_api_route('/ping', ping_router.ping, methods=['GET'])