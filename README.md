# Elasticsearch + Kibana in Docker and Podman

## Run project
### Docker

    docker-compose up -d

### Podman
    . podman.sh

## Access Elasticsearch

    http://localhost:9200/

## Access Kibana

    http://localhost:5601/

## Add records

Refer to [request.py](request.py) for adding records to elasticsearch from:

* Python dict
* CSV file
* JSON file

## Podman commands
Stop pod

    podman pod stop elk

Create config file for Kubernetes

    podman generate kube elk

List of pods and containers

    podman ps -a --pod

Find out which user the image "wants" to run as

    podman run --rm --entrypoint '' <image> id

Container processes
    
    podman top <container_name>

Stop pod

    alias stop='podman pod stop <pod_name> && podman pod rm <pod_name>'