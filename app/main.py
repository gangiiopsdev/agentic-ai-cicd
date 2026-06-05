from fastapi import FastAPI
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            output = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE)
            return await output.communicate()
        except Exception as e:
            return str(e)
global_app = FastAPI()

global_app.get("/ping")(
    response_model=str,
    summary="Ping a host",
    description="Ping a specified host to check connectivity.",
    async def ping(host: str):
        # Sanitize the input
        if not host.isalnum():
            return "Invalid hostname"
        command = PingCommand(host)
        return await command.execute())