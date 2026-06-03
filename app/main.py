from fastapi import FastAPI
import ping3

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            response_time = await ping3.ping(self.host)
            return {'status': 'completed', 'response_time': response_time}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    return ping_command.execute().result()