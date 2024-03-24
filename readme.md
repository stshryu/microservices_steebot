# Microservices Steebot

An exercise in creating small lightweight microservices.

## Setup

Run `docker-compose up --build` and the project will spin up the required services.

Currently, the build only creates a persistent store and redis server. If you want to create the full stack application use the profile flag 

`docker-compose --profile frontend --profile toxicticket up`

## Project Layout

`client/` contains the frontend built in React.

`toxic_ticket/` contains the `toxicticket` compose service profile. This is the endpoint that allows admins to assign tickets and ticket counts to users.

`discord_wrapper/` contains the `discordwrapper` compose service profile. This is the main wrapper that translates commands from Discord and creates events/jobs in the relevant redis queues to be picked up by the various microservices.

## Caveats

Keep in mind that currently we're using a **single** MongoDB instance and using discrete collections from it. While I've made sure that there is no overlap, or crossover between our microservices and their respective collections they access, for production you would want to split separate MongoDB instances for each service.

In other words `toxic_ticket` would have its own Mongo instance called `tt_mongodb` and `discord_wrapper` should have its own instance called `dw_mongodb`. 

This ensures that if for whatever reason `toxic_ticket`'s `tt_mongodb` instance is down `discord_wrapper` isn't directly affected. Obviously, if you attempted to create, remove or edit toxic tickets that wouldn't work until the server is back up and running, but because we decoupled both these services from each other `discord_wrapper` is in no way dependent on `toxic_ticket` being up and running to work normally.

