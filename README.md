# TAPO TP100 REMOTE CONTROL FUNCTION
Docker service to switch TAPO-P100 plugs. To be deployed in RaspberryPI inside the network.

### DEPLOY

Build the docker image

```
docker build -t tapo .
```

Run it:

```
docker run -p 80:5000 tapo
```

### TEST

```
http://localhost:80/api/P100?state=0&address=<IP_ADDRESS>&email=<EMAIL>&password=<PASS>
```

### NOTES

A ready made Raspberry PI docker image is available here: https://hub.docker.com/repository/docker/luisalvesmartins/tapo-p100

Unsecure solution to be used indoor only.

Connection to the plug can be stored inside the container and not passed thru the network.


### ORIGINAL CODE FROM k4czp3r

Added the webservice and docker component to the work from k4czp3r:

https://k4czp3r.xyz/posts/reverse-engineering-tp-link-tapo/

https://github.com/K4CZP3R/tapo-p100-python