from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.ping_command = ['ping', '-c', '4']

    async def execute_ping(self, host: str):
        args = self.ping_command + [shlex.quote(host)]
        try:
            result = await asyncio.create_subprocess_exec(*args,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
            output, error = await result.communicate()
            return output.decode(), error.decode()
        except Exception as e:
            return None, str(e)
class App:
    def __init__(self):
        self.safe_ping = SafePing()

    async def ping(self, host: str):
        output, error = await self.safe_ping.execute_ping(host)
        if error:
            return {'status': 'failed', 'error': error}
        else:
            return {'status': 'completed', 'output': output}
app = App()

@app.get('/ping')
def ping_endpoint(host: str):
    return app.ping(host)