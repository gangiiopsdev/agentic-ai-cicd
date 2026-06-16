from fastapi import FastAPI
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            args = ['ping', self.host]
            result = subprocess.run(args, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    return command.execute()