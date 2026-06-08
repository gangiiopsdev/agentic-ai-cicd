from fastapi import FastAPI
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        return os.system(f'ping {shlex.quote(self.host)}')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    result = command.execute()
    return {'status': 'completed', 'output': result}