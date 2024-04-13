# Microservices Steebot

An exercise in creating small lightweight microservices.

## Setup

Run `docker-compose up --build` and the project will spin up the required services.

Currently, the build only creates a persistent store and redis server. If you want to create the full stack application use the profile flag 

`docker-compose --profile dev up`

You can check the `docker-compose.yml` file to see all the profile tags, you can chain the profile flag calls to selectively call up certain containers. 

Keep in mind that mongodb and redis are spun up no matter what, those are core services that need to be running for any container to successfully run.

A sample `.env` file is shown in the root of the project called `.env.sample`. It holds all the keys we expect to see in the `.env.dev` or `.env.prod` files that the individual services will require to run.

For example, each `toxic_ticket/` and `discord_wrapper/` should each have their own respective `.env..dev` files.

## Project Layout

`client/` contains the frontend built in React.

`toxic_ticket/` contains the `toxicticket` compose service profile. This is the endpoint that allows admins to assign tickets and ticket counts to users.

`discord_wrapper/` contains the `discordwrapper` compose service profile. This is the main wrapper that translates commands from Discord and creates events/jobs in the relevant redis queues to be picked up by the various microservices.

## Testing

Running the tests for each individual service is simple.

The tests are contained in the `{root}/tests` folder, which means toxic ticket and discord wrapper will have their tests located in `toxic_ticket/tests` and `discord_wrapper/tests` respectively.

Once the container is running (either as a daemon, on the dashboard or in the terminal) run the following command:

`docker-compose exec {container_name} python3 -m pytest tests`

This will execute `pytest` for the specified container.

Compose aliases and full project testing TBA.

## Caveats

Keep in mind that currently we're using a **single** MongoDB instance and using discrete collections from it. While I've made sure that there is no overlap, or crossover between our microservices and their respective collections they access, for production you would want to split separate MongoDB instances for each service.

In other words `toxic_ticket` would have its own Mongo instance called `tt_mongodb` and `discord_wrapper` should have its own instance called `dw_mongodb`. 

This ensures that if for whatever reason `toxic_ticket`'s `tt_mongodb` instance is down `discord_wrapper` isn't directly affected. Obviously, if you attempted to create, remove or edit toxic tickets that wouldn't work until the server is back up and running, but because we decoupled both these services from each other `discord_wrapper` is in no way dependent on `toxic_ticket` being up and running to work normally.

