from fastapi import FastAPI
import os

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            response = os.system('ping -c 4 ' + self.host)
            return response == 0, '' if response == 0 else 'Ping failed'
        except Exception as e:
            return False, str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    success, message = command.execute()
    return {'status': 'completed', 'success': success, 'message': message}