from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        escaped_host = ''.join(c for c in host if c.isalnum() or c in ('.', '-', '_'))
        command = ['ping', escaped_host]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        return {'status': 'completed', 'output': output.decode(), 'error': error.decode()}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return SafeSubprocess.ping(host)