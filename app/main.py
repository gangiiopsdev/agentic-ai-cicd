from fastapi import FastAPI
import subprocess
class PingHandler:
    def ping(self, host: str):
        try:
            output = subprocess.check_output(['ping', '-c', '1', '--', host], stderr=subprocess.STDOUT)
            return output.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return f'Ping failed with error: {e.output.decode('utf-8')}'

app = FastAPI()
c_handler = PingHandler()

@app.get("/ping")
def ping(host: str):
    if not self.is_valid_host(host):
        raise ValueError('Invalid host')
    return c_handler.ping(host)

@staticmethod
def is_valid_host(host: str) -> bool:
    import re
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return bool(pattern.match(host))