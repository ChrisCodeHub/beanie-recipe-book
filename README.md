# beanie-recipe-book
This is just a "play around and see what I can get working project"
Idea is to creare a basic app that
it is indeed a recipe book using beanie, mongo and fastAPI
Step 1 
  is to get MongoDB running in a Docker contaniner, with volume to give disk backing 
  Beanie python container talking to it and just populating a basic collection
Step 2 
  Add fast API so that REST API can be added to retrieve / update / delete recipes
  turn into Docker Compose
Step 3
  move from Docker Compose to k3s
Step 4
  add a basic React/Vue front end


# Notes
Getting mongoDB running


step 1 - 
- just spin up a pre-packed docker from docker-hub
- since this is runing in detached mode, connect to explore using the mongosh utilty
- stop and remove when done
```
docker run --name mongodb -d mongo:6.0
docker exec -it mongodb bash
docker stop mongodb && docker rm mongodb
```

OK - need some username/password action to toughen up the connections, keep out the pixies
add admin::unicorn  password::fairydust

```
docker run --name mongodb -d \ 
        -e MONGO_INITDB_ROOT_USERNAME=unicorn \
	      -e MONGO_INITDB_ROOT_PASSWORD=fairydust \
        mongo:6.0
```



