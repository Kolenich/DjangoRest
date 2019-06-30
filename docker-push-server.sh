#!/usr/bin/env bash
docker build -t server -f Dockerfile.server .
docker tag server kolenich/server
docker push kolenich/server
