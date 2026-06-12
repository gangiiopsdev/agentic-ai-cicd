from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        if self.validate_host():
            command = ['ping', self.host]
            try:
                output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=False)
                return output.decode('utf-8')
            except subprocess.CalledProcessError as e:
                return e.output.decode('utf-8')
        else:
            return "Invalid host"

    def validate_host(self):
        allowed_hosts = ['127.0.0.1', 'localhost']  # Example validation logic
        return self.host in allowed_hosts