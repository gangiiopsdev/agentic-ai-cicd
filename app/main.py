from fastapi import FastAPI
import subprocess
class Ping:
    def __init__(self):
        self.host = None

    def set_host(self, host: str):
        self.host = host

    def execute(self):
        try:
            result = subprocess.check_output(['ping', self.host], stderr=subprocess.STDOUT)
            return {'status': 'completed', 'result': result.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'error': e.output.decode('utf-8')}