#!/usr/bin/env bash
docker build -t server .
docker tag server kolenich/server
docker push kolenich/server
