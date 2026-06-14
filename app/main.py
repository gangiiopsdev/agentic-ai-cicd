from fastapi import FastAPI
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            # Validate the host input to prevent command injection
            if not self.host.isalnum():
                raise ValueError('Invalid host input')
            output = await asyncio.create_subprocess_exec('ping', self.host,
                                                       stdout=subprocess.PIPE,
                                                       stderr=subprocess.PIPE)
            stdout, stderr = await output.communicate()
            return {'status': 'completed', 'output': stdout.decode()}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    ping_command = PingCommand(host)
    return ping_command.execute()