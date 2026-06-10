from fastapi import FastAPI
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        args = ['ping', self.host]
        subprocess.run(args, check=True, shell=False)

def ping(host: str):
    return PingCommand(host).execute()

app = FastAPI()

@app.get('/ping')
def ping_host(host: str):
    try:
        return ping(host)
    except Exception as e:
        return {'error': str(e)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}