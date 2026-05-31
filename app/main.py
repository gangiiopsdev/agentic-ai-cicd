from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.ping_command = ['ping']

    async def ping_host(self, host: str):
        if not self._is_safe_hostname(host):
            raise ValueError('Invalid hostname')
        args = self.ping_command + [host]
        return await self.run_subprocess(args)

    @staticmethod
    def _is_safe_hostname(hostname: str) -> bool:
        # Simple check to ensure the hostname does not contain potentially dangerous characters
        return all(c.isalnum() or c in ('.', '-') for c in hostname)

    async def run_subprocess(self, args: list):
        result = await subprocess.run(args, capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else None

class PingRouter:
    def __init__(self):
        self.safe_ping = SafePing()

    @staticmethod
    async def get(host: str):
        try:
            output = await PingRouter().safe_ping.ping_host(host)
            if output:
                return {'status': 'completed', 'result': output}
            else:
                return {'error': 'Failed to ping the host'}
        except ValueError as e:
            return {'error': str(e)}

app = FastAPI()

ping_router = PingRouter()
app.add_api_route('/ping', ping_router.get, methods=['GET'])