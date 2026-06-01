from fastapi import FastAPI
import subprocess
class PingHandler:
    def __init__(self):
        self.app = FastAPI()
        self.app.get "/ping"(self.ping)

    async def ping(self, host: str):
        try:
            output = await asyncio.create_subprocess_exec('ping', host,
                                                        stdout=subprocess.PIPE,
                                                        stderr=subprocess.PIPE,
                                                        text=True)
            return {'status': 'completed', 'output': output.stdout}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}
ping_handler = PingHandler().app