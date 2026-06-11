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