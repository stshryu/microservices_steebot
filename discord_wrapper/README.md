# Discord Wrapper Server

FastAPI server designed to act as a wrapper to `discord.py` to allow commands in and out of the discord server.

## Functionality

Runs on port `5000`.

Currently supports these commands:

1. `!tt add {user}` - Add a toxic ticket to specified user
2. `!tt remove {user}` - Remove a toxic ticket from a specified user
3. `!tt {user}` - Get the user and their current toxic ticket count

## Server Communication

This server requires `toxic_ticket` to also be running in order to ingest and execute the desired commands.

If you run this server standalone, the process will still continue like normal and will output results to the redis queue, but the executed commands will not trigger until `toxic_ticket` is run, and ingests the jobs in the queue.
