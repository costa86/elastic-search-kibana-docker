#variables
POD=elk
ES_PORT=9200
KIBANA_PORT=5601
ES_IMAGE=elasticsearch:7.14.1
KIBANA_IMAGE=kibana:7.14.1
ES_VOLUME_FOLDER=es_data

#create ES data folder
if [ ! -d "$ES_VOLUME_FOLDER" ]; then
    mkdir ${ES_VOLUME_FOLDER}
fi

#pod
podman pod create --name ${POD} -p ${KIBANA_PORT}:${KIBANA_PORT} -p ${ES_PORT}:${ES_PORT}

#kibana
podman run --pod=$POD \
-e ELASTICSEARCH_HOSTS=http://localhost:${ES_PORT} \
--name kibana \
--user ${UID} \
-d ${KIBANA_IMAGE}

#ES
podman run --pod=$POD \
-e discovery.type=single-node \
-e xpack.security.enabled=false \
-v ${PWD}/${ES_VOLUME_FOLDER}:/usr/share/elasticsearch/data \
--name es \
--user ${UID} \
-d ${ES_IMAGE}
