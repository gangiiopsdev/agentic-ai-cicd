async def run_command(self, command: str, allowed_hosts: List[str] = None):
        if not self.is_allowed_command(command, allowed_hosts):
            raise ValueError('Invalid command')
        process = await asyncio.create_subprocess_exec(
            *command.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        return stdout.decode(), stderr.decode()