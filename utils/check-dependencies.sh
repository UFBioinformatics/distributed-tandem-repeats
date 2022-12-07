#!/usr/bin/env bash

# DO NOT CALL THIS SCRIPT DIRECTLY. ONLY USE MAKE COMMANDS

source './env.sh'

if ! docker info > /dev/null 2>&1; then
  echo "> This script uses docker, and it isn't running - please start docker and try again!"
  exit 1
fi
if [ "$( docker container inspect -f '{{.State.Running}}' $container_name )" != "true" ] > /dev/null 2>&1; then
  echo "> This script uses $container_name container, and it isn't running - please start $container_name and try again!"
  exit 1
fi