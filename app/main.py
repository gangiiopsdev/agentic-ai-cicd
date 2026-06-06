from fastapi import FastAPI
import subprocess
class PopenWrapper:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.process = None

    def run(self):
        if 'shell' in self.kwargs and self.kwargs['shell'] is True:
            raise ValueError('Shell execution is not allowed')
        for arg in self.args:
            if isinstance(arg, str) and any(char.isdigit() for char in arg):
                raise ValueError('Command injection detected')
        self.process = subprocess.Popen(*self.args, **self.kwargs)
        return self.process

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host in ['localhost', '127.0.0.1']:
        # Validate the input to prevent command injection
        if host.strip() == host and not any(char.isdigit() for char in host):
            wrapper = PopenWrapper(['ping', host])
            wrapper.run()
            return {'status': 'completed'}
    else:
        return {'status': 'error', 'message': 'Invalid hostname'}