from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    args = ['ping', '-c', '1', host]  # Limit the number of pings and use only one IP address
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout

class SafePingFastAPI(FastAPI):
    def __init__(self):
        super().__init__()
        self.add_api_route('/ping', self.ping)

    async def ping(self, host: str):
        try:
            result = safe_ping(host)
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'result': e.stderr}
        return {'status': 'completed', 'result': result}

app = SafePingFastAPI()