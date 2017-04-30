#!/bin/sh
VERSION="1.0.0-SNAPSHOT"
AUTHOR="Zak Hassan <zak.hassan@redhat.com>"
COMPONENT=""

cat << 'EOF'
    _   __      __       __                __
   / | / /___  / /____  / /_  ____  ____  / /__
  /  |/ / __ \/ __/ _ \/ __ \/ __ \/ __ \/ //_/
 / /|  / /_/ / /_/  __/ /_/ / /_/ / /_/ / ,<
/_/ |_/\____/\__/\___/_.___/\____/\____/_/|_|
    ____        __    ___      __
   / __ \__  __/ /_  / (_)____/ /_  ___  _____
  / /_/ / / / / __ \/ / / ___/ __ \/ _ \/ ___/
 / ____/ /_/ / /_/ / / (__  ) / / /  __/ /
/_/    \__,_/_.___/_/_/____/_/ /_/\___/_/
EOF

docker   build  --rm   -t  notebook-ws .
docker tag  notebook-ws  docker.io/zmhassan/notebook-ws
docker push  docker.io/zmhassan/notebook-ws

echo "Image pushed..."