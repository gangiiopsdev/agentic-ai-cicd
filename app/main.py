from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            result = await self.run_command()
            return result
        except Exception as e:
            return str(e)

    async def run_command(self):
        command = ['ping', '-c', '1', self.host]  # Assuming ping should only send one packet
        process = await asyncio.create_subprocess_exec(*command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await process.communicate()
        if process.returncode != 0:
            return {'status': 'failed', 'error': stderr.decode()}
        return {'status': 'completed', 'output': stdout.decode()}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        command = PingCommand(host)
        result = command.execute()
        if isinstance(result, dict) and result['status'] == 'failed':
            return {'status': result['status'], 'error': result['error']}
        else:
            return result
    except Exception as e:
        return {'status': 'error', 'message': str(e)}