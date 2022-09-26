# Pokemon API Demo
Retrieves a subset of data on a provided list of pokemon names

The names retrieved are hard-coded for simplicity and can be updated
by editing the ```pokemon_list``` variable

By default this server will run on localhost:5000 and the endpoint is reachable at api/pokedex



Install dependencies

```$ pip install -r requirements.txt```

Configure Flask environment variables:

1. Required
   1. FLASK_APP=app.py
2. Optional
   1. FLASK_DEBUG=True
   2. FLASK_ENV=development
