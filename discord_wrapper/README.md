# Discord Wrapper Server

FastAPI server designed to act as a wrapper to `discord.py` to allow commands in and out of the discord server.

## Functionality

Runs on port `5000`.

Currently supports these commands:

1. `!tt add {user}` - Add a toxic ticket to specified user
2. `!tt remove {user}` - Remove a toxic ticket from a specified user
3. `!tt {user}` - Get the user and their current toxic ticket count

## Server Communication

This server requires `toxic_ticket` to also be running in order to ingest and execute the desired commands. Because of the nature of the pub/sub connection between the two services if both are not running the `publish()` method will not actually output the data anywhere, and will be lost if a subscriber is not listening to the channel.

Keep in mind our services use redis to communicate with each other. This means that from the `discord_wrapper` server we need to publish to a channel that the `toxic_ticket` server can subscribe to.

We use a variable called `TOXIC_TICKET_CHANNEL={channel_id}` in our `.env.dev` within both servers. This will be used to initialize our pub/sub channel to allow connection between the two servers. 
