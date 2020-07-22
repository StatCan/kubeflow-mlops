#!/bin/bash
while getopts "r:" option;
    do
    case "$option" in
        r ) REGISTRY_NAME=${OPTARG};;
    esac
done
IMAGE=${REGISTRY_NAME}.azurecr.io/tensorflow-training
docker build -t $IMAGE . && docker run -it $IMAGE
