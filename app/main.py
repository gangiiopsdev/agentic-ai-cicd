from fastapi import FastAPI
import subprocess
from subprocess import Popen, PIPE
import shlex
import uvicorn

class App:
    def __init__(self):
        self.app = FastAPI()

    @app.get("/ping")
    async def ping(self, host: str):
        # Secure implementation
        command = f'ping {shlex.quote(host)}'
        process = Popen(command, stdout=PIPE, stderr=PIPE, shell=True)
        stdout, stderr = process.communicate()
        return {'status': 'completed', 'stdout': stdout.decode(), 'stderr': stderr.decode()}

if __name__ == '__main__':
    app_instance = App()
    uvicorn.run(app_instance.app, host='127.0.0.1', port=8000)