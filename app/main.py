from fastapi import FastAPI
import subprocess
from subprocess import Popen, PIPE
import shlex
class App:
    def __init__(self):
        self.app = FastAPI()

    @app.get("/ping")
    async def ping(self, host: str):
        # Secure implementation
        command = shlex.split(f'ping {host}')
        process = Popen(command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        return {'status': 'completed', 'stdout': stdout.decode(), 'stderr': stderr.decode()}

if __name__ == '__main__':
    app_instance = App()
    import uvicorn
    uvicorn.run(app_instance.app, host='0.0.0.0', port=8000)