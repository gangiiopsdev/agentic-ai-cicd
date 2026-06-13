from fastapi import FastAPI
import asyncio
import re
import shlex
class SafePing:
    @staticmethod
def safe_ping(host: str):
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid hostname')
        args = ['ping', '-c', '1', shlex.quote(host)]
        result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return await result.communicate()
class PingAPI:
    app = FastAPI()

    @app.get('/')
def home():
        return {'message': 'Agentic Self-Healing Pipeline'}

    @app.get('/ping')
def ping(host: str):
        try:
            stdout, stderr = SafePing.safe_ping(host)
            if stderr:
                return {'status': 'error', 'stderr': stderr.decode()}
            else:
                return {'status': 'completed', 'stdout': stdout.decode()}
        except Exception as e:
            return {'status': 'error', 'error': str(e)}