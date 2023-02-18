#!/bin/bash

minikube start
minikube kubectl -- apply -f ./pingpong.yaml
minikube tunnel &
sleep 20
python3 ./testServer.py
