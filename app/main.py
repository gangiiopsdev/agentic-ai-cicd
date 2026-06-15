from fastapi import FastAPI
import subprocess
import shlex
import re

class App:
    def __init__(self):
        self.app = FastAPI()

    @app.get("/ping")
    def ping(self, host: str):
        # Define a regular expression for allowed characters in the hostname
        pattern = re.compile(r'^[a-zA-Z0-9.-_]+$')
        if not pattern.match(host):
            return {'status': 'invalid_host'}

        command = ["ping", host]
        subprocess.run(command, check=True)
        return {"status": "completed"}

app = App().app