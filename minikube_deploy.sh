#!/bin/bash
kubectl create secret generic postgres-credentials \
    --from-literal=username=$DB_USERNAME \
    --from-literal=password=$DB_PASSWORD

kubectl apply -f kubernetes