from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        args = ['ping', host]
        try:
            result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return f'Error: {e.stderr.decode('utf-8')}'

app = FastAPI()

def ping(host: str):
    # Safe implementation
    response = SafePing.safe_ping(host)
    return {'status': 'completed', 'output': response}