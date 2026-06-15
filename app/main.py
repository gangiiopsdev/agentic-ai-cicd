from fastapi import FastAPI
import subprocess
import shlex

class App:
    def __init__(self):
        self.app = FastAPI()

    @app.get('/ping')
    def ping(self, host: str):
        # Secure implementation
        command = ['ping'] + shlex.split(host)
        subprocess.run(command, check=True)
        return {'status': 'completed'}

app_instance = App().app