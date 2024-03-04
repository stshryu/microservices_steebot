# Discord API Wrapper

This is going to be the base API server we used to communicate with the wrapper as well as handle auth and database transactions.

Written using FastAPI, there was some considerations into using Flask or Django, however the use case we want is extremely performant, small and scalable server, which means we don't need any extra goodies like Jinja or HTML templating responses from Flask/Django.


