from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def execute(host):
        try:
            # Use subprocess.run instead of subprocess.call
            result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode()
        except subprocess.CalledProcessError as e:
            return str(e)

class PingEndpoint:
    @staticmethod
def ping(host: str):
        # Call the PingCommand class method instead of using subprocess directly
        return {'status': 'completed', 'output': PingCommand.execute(host)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    return PingEndpoint.ping(host)