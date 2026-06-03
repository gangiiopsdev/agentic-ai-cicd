from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    def __init__(self):
        self.safe_hosts = ['127.0.0.1', '::1']  # Add more trusted hosts as needed

    def is_safe_host(self, host):
        return host in self.safe_hosts

    def run_command(self, command, args):
        if not self.is_safe_host(command):
            raise ValueError('Command is not allowed')
        safe_command = subprocess.list2cmdline([command])
        subprocess.run([safe_command] + args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()
safe_subprocess = SafeSubprocess()

@app.get('/ping')
def ping(host: str):
    safe_subprocess.run_command('ping', [host])
    return {'status': 'completed'}