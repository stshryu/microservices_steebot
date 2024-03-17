# Microservices Steebot

An exercise in creating small lightweight microservices.

## Setup

Run `docker-compose up --build` and the project will spin up the required services.

Currently, the build only creates a persistent store and redis server. If you want to create the full stack application use the profile flag 

`docker-compose --profile frontend --profile toxicticket up`

## Project Layout

`client/` contains the frontend built in React.

`toxic_ticket/` contains the `toxicticket` compose service profile. This is the endpoint that allows admins to assign tickets and ticket counts to users.

## TODO

Eventually, we want everything to communicate through Redis, where possible. The project communication should look like so:

1. Discord admin types `!tt @discord_username`
2. Main server receives message sent event and publishes a notification to the `toxic_ticket` queue
3. Toxic Ticket server reads the job from the `toxic_ticket` queue and processes the request

As it stands, we have standalone servers and services (toxicticket for example) but we'll eventually want to move towards a decoupled pub/sub architecture.
