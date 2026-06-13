from fastapi import FastAPI
import subprocess
import shlex

class PingApp:
    def __init__(self):
        self.app = FastAPI()

    def ping(self, host: str):
        args = ['ping'] + shlex.split(host)
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed'}

if __name__ == '__main__':
    app_instance = PingApp()
    app = app_instance.app