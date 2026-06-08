from fastapi import FastAPI
import asyncio
def ping(host: str):
    if host in denied_hosts:
        return {'status': 'error', 'message': 'Host is not allowed'}

    args = ['ping', host]
    result = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
    stdout = await result.stdout.read()
    return {'status': 'completed', 'stdout': stdout}