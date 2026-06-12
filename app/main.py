from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        command = ['ping', self.host]
        try:
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=False)
            return output.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return e.output.decode('utf-8')

# Add input validation for host parameter to ensure it does not contain malicious content
def validate_host(host: str) -> bool:
    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-")
    return all(char in allowed_chars for char in host)

app = FastAPI()
@app.post('/ping/')
def ping(host: str):
    if validate_host(host):
        return PingCommand(host).execute()
    else:
        raise ValueError('Invalid input')