from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def call(command: str, *args, **kwargs):
        safe_command = [arg for arg in command.split(' ') if arg]
        return subprocess.run(safe_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
app = FastAPI()
def escape_host(host):
    return ''.join(c for c in host if c.isalnum() or c in '-._')
@app.get('/ping')
def ping(host: str):    safe_host = escape_host(host)    try:
        result = SafeSubprocess.call(f'ping {safe_host}', shell=False)
        output = result.stdout.decode('utf-8')
        return {
            'status': 'completed',
            'message': f'Pinged host: {safe_host}
Output: {output}'
        }
    except subprocess.CalledProcessError as e:
        return {
            'status': 'error',
            'message': f'Ping failed for host: {safe_host}
Error: {e.stderr.decode('utf-8')}'
        }