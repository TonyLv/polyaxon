---
title: "Outputs on NFS"
meta_title: "NFS"
meta_description: "Using NFS to organize your jobs outputs and experiment artifacts. Polyaxon allows users to connect to one or multiple NFS servers to store job outputs and experiment artifacts."
custom_excerpt: "The Network File System (NFS) is a client/server application that lets a computer user view and optionally store and update files on a remote computer as though they were on the user's own computer."
image: "../../content/images/integrations/nfs.png"
author:
  name: "Polyaxon"
  slug: "Polyaxon"
  website: "https://polyaxon.com"
  twitter: "polyaxonAI"
  github: "polyaxon"
tags: 
  - artifacts-store
  - storage
featured: false
visibility: public
status: published
---

## Overview

This guide shows how to use an NFS server to mount a volume to collect outputs and artifacts of your jobs and experiments.
 
This guide uses the [click-to-deploy single-node file server](https://console.cloud.google.com/marketplace/details/click-to-deploy-images/singlefs) 
on Google Cloud Platform to create a ZFS file server running on a single Google Compute Engine instance, but the same principle applies to an NFS server running on any platform. 

## Create a Single Node Filer

Using [click-to-deploy single-node file server](https://console.cloud.google.com/marketplace/details/click-to-deploy-images/singlefs), 
you need to create a filer: `polyaxon-nfs`, and keep the default value `data`, and check `enable NFS sharing`. You can set the storage to 50GB for example.

## Create a folder for hosting your outputs

Use ssh to create a folder for your outputs `plx-outputs` under `/data`:

```bash
gcloud --project "polyaxon-test" compute ssh --ssh-flag=-L3000:localhost:3000 --zone=us-central1-b polyaxon-nfs-vm
```
```bash
cd /data
```
```bash
mkdir -m 777 plx-outputs
```

## Get the ip address of the filer

```bash
gcloud --project "polyaxon-test" compute instances describe polyaxon-nfs-vm --zone=us-central1-b --format='value(networkInterfaces[0].networkIP)'
```

> You might need to use the correct project name and zone.

## Create a PVC with the correct ip addresses

Create `outputs-pvc.yml` containing the following PVS definition:

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: polyaxon-pv-outputs
spec:
  capacity:
    storage: 45Gi
  accessModes:
    - ReadWriteMany
  nfs:
    server: 10.138.0.3  # Use the right IP
    path: "/data/plx-outputs"
  claimRef:
    namespace: polyaxon
    name: polyaxon-pvc-outputs
---
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: polyaxon-pvc-outputs
spec:
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 45Gi
```

## Use kubectl to create the PVC based on the nfs server

Under the same namespace where you are deploying Polyaxon, e.g. `polyaxon`, create the PVC using kubectl

```bash
kubectl create -f outputs-pvc.yml -n polyaxon
```

## Now you can use this PVC to mount the outputs volume to your experiments and jobs in Polyaxon

```yaml
outputs:
  plx-outputs:
    existingClaim: polyaxon-pvc-outputs
    mountPath: /plx-outputs
```
