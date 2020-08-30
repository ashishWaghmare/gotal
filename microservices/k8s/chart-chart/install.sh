#!/bin/bash -ex

for d in $(find services/charts/ -type d -mindepth 1 -maxdepth 1); do
    echo $d
    (cd $d && helm dep up)
done

helm upgrade --install myrelease . 