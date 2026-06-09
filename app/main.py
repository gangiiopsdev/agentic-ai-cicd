from fastapi import FastAPI
import asyncio
import re
import ipaddress

class PingHost:
    def __init__(self, host):
        self.host = host

    async def ping(self):
        result = await asyncio.create_subprocess_exec('ping', self.host, check=True)
        return await result.wait()

class PingEndpoint:
    @staticmethod
    def ping(host: str):
        try:
            # Validate the host input using a whitelist or regex
            ipaddress.ip_address(host)  # Use ipaddress to validate IPs and domain names safely
        except ValueError as e:
            return {'error': str(e)}, 400

        pinger = PingHost(host)
        try:
            result = await pinger.ping()
            return {'status': 'completed'}
        except asyncio.subprocess.CalledProcessError as e:
            return {'error': f'Ping failed: {e}'}, 500

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return PingEndpoint.ping(host)