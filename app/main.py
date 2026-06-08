from fastapi import FastAPI
import subprocess
import shlex
class SafePinger:
    def __init__(self, hosts):
        self.hosts = hosts.split(',').strip()

    async def ping_hosts(self):
        results = {}
        for host in self.hosts:
            if not self.is_valid_host(host.strip()):
                results[host] = {'status': 'failed', 'error': 'Invalid host'}
                continue
            try:
                result = subprocess.run(['ping', '-c', '1'] + shlex.split(host), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                results[host] = {'status': 'completed', 'output': result.stdout.decode()}
            except subprocess.CalledProcessError as e:
                results[host] = {'status': 'failed', 'error': e.stderr.decode()}
        return results

    def is_valid_host(self, host):
        allowed_hosts = ['192.168.0.1', '192.168.0.2', 'localhost']
        return host in allowed_hosts
app = FastAPI()
pinger = SafePinger(hosts='192.168.0.1,192.168.0.2')
@app.get('/ping_all')
def ping_all_hosts():
    return pinger.ping_hosts()