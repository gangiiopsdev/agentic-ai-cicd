from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def safe_command(command, *args):
        if not all(arg.isalnum() for arg in args):
            raise ValueError('Invalid arguments provided')
        full_command = [command] + list(args)
        subprocess.run(full_command, check=True, shell=False)

app = FastAPI()

def ping(host: str):
    SafeSubprocess.safe_command('ping', host)

@app.get('/ping')
def ping_endpoint(host: str):
    return {'result': ping(host)}