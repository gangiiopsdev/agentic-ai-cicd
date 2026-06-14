from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.ping_command = ['ping', 'localhost']

    async def ping(self, host: str):
        try:
            output = await asyncio.create_subprocess_exec(*self.ping_command + [host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = await output.communicate()
            return stdout.decode().strip(), stderr.decode().strip()
        except Exception as e:
            return f'Ping failed: {str(e)}'

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    output, error = safe_ping_instance.ping(host)
    return {'status': 'completed', 'output': output, 'error': error}