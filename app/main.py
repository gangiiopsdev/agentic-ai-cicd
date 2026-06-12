from fastapi import FastAPI
import subprocess
class CommandExecutor:
    def __init__(self, command: str):
        self.command = command

    def run(self):
        try:
            result = subprocess.run(self.command.split(), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return str(e.stderr.decode('utf-8'))

app = FastAPI()

allowed_hosts = ['example.com', 'test.com']
def validate_host(host):
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    executor = CommandExecutor(['ping', host])
    return {'status': 'completed', 'output': executor.run()}