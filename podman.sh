#variables file
ENV_FILE=env.env

get_var_from_env_file () {
    echo $(grep $1 ${ENV_FILE} | cut -d '=' -f2)
}

#variables from env file
POD=$(get_var_from_env_file POD)
ES_PORT=$(get_var_from_env_file ES_PORT)
KIBANA_PORT=$(get_var_from_env_file KIBANA_PORT)
ES_IMAGE=$(get_var_from_env_file ES_IMAGE)
KIBANA_IMAGE=$(get_var_from_env_file KIBANA_IMAGE)
ES_VOLUME_FOLDER=$(get_var_from_env_file ES_VOLUME_FOLDER)

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
