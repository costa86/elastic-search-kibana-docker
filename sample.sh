ENV_FILE=env.env

read_from_env () {
    echo $(grep $1 ${ENV_FILE} | cut -d '=' -f2)
}

POD=$(read_from_env "POD")
ES_PORT=$(read_from_env "ES_PORT")
KIBANA_PORT=$(read_from_env "KIBANA_PORT")
ES_IMAGE=$(read_from_env ES_IMAGE)
KIBANA_IMAGE=$(read_from_env "KIBANA_IMAGE")
ES_VOLUME_FOLDER=$(read_from_env "ES_VOLUME_FOLDER")

echo $ES_IMAGE