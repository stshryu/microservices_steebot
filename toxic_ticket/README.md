# Basic User and Toxic Ticket functionality

FastAPI server designed to ingest jobs from a redis queue to `add`, `remove` and `view` toxic tickets that have been assigned to a user.

## Functionality

Runs on port `5001`.

Currently will ingest jobs from the redis queue and execute them.

Contains methods for a `user` object that stores the username, email and toxic ticket count.

## API 

The toxic ticket API endpoint can be reached directly, if you have the proper credentials that wraps the endpoints. There's no auth on admin or user currently so its a moot point, but when it is added it should only allow interfacing through the queue.
