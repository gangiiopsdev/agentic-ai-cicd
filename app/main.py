from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_call(command, *args):
        process = subprocess.Popen(command,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode(), stderr.decode()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = ['ping', host]
    stdout, stderr = SafePing.safe_call(command)
    return {'status': 'completed', 'stdout': stdout, 'stderr': stderr}