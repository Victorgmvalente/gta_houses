#!/bin/bash -xe

basedir="$(dirname "$0")"

cmd_image() {
  docker build -t "$USER:latest" .
}

cmd_stop() {
  docker rm "$USER" -f || true
}

cmd_run() {
  docker run -it --rm --name "$USER" \
  -v "$PWD:/$USER/" \
  -p 8085:8085 \
  -p 5000:5000 \
  -p 4141:4141 \
  "$USER:latest" "/$USER/entrypoint/jupyter.sh"
}

cmd_exec() {
  docker exec -it "$USER" "$@"
}

cmd_entrypoint() {
  _entrypoint=${1?'command'}
  shift
  cmd_exec "/opt/$USER/entrypoint/$_entrypoint.sh" "$@"
}

_cmd=${1?'command'}
shift
cmd_${_cmd} "$@"
