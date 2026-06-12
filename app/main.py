from fastapi import FastAPI
import subprocess
def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error
class PingRouter:
    def __init__(self):
        self.allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts

    async def ping(self, host: str):
        if host in self.allowed_hosts:
            output, error = run_command(['ping', host])
            return {'status': 'completed', 'output': output.decode(), 'error': error.decode()}
        else:
            return {'status': 'failed', 'message': 'Host not allowed'}

app = FastAPI()
ping_router = PingRouter()
app.add_api_route('/ping', ping_router.ping, methods=['GET'])