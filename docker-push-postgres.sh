#!/usr/bin/env bash
docker build -t postgres -f Dockerfile.postgres .
docker tag postgres kolenich/postgres
docker push kolenich/postgres
