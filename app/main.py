from fastapi import FastAPI
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        return await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the input to ensure it's a valid hostname/IP address
    import ipaddress
    try:
        ipaddress.ip_address(host)
    except ValueError:
        return {'error': 'Invalid host'}

    command = PingCommand(host)
    result = await command.execute()
    return {'status': 'completed', 'output': result.stdout.decode() if result.stdout else ''}