from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            # Sanitize input to prevent command injection
            result = await asyncio.create_subprocess_exec('ping', '-c', '1', self.host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = await result.communicate()
            if result.returncode != 0:
                return {'status': 'failed', 'error': error.decode()}
            return {'status': 'completed', 'output': output.decode()}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}