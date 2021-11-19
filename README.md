# Elasticsearch + Kibana in Docker

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