from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        if host in ['localhost', '127.0.0.1']:  # Allow only specific hosts for security reasons
            command = ["ping", host]
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
            return output.decode(), error.decode()
        else:
            raise ValueError('Invalid host')

app = FastAPI()

def ping(host: str):
    result = SafePing.safe_ping(host)
    return {"status": "completed", "output": result[0], "error": result[1]}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)