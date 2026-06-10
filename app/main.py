from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, allowed_networks):
        self.allowed_networks = allowed_networks

    def execute(self, host):
        for network in self.allowed_networks:
            if host.startswith(network):
                try:
                    result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
                    return {'status': 'completed', 'output': result.stdout}
                except subprocess.CalledProcessError as e:
                    return {'error': str(e)}
            else:
                return {'error': 'Invalid host address'}

app = FastAPI()
ping_command = PingCommand(['192.168.', '172.'])

@app.get("/ping")
def ping(host: str):
    return ping_command.execute(host)