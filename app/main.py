from fastapi import FastAPI
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            result = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = await result.communicate()
            return stdout.decode(), stderr.decode()
        except Exception as e:
            return None, str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isnumeric():  # Basic validation to avoid command injection
        return {'status': 'failed', 'error': 'Invalid host'}
    command_executor = PingCommand(host)
    output, error = command_executor.execute()
    if error:
        return {'status': 'failed', 'error': error}
    return {'status': 'completed', 'output': output}