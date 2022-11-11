![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![Amp](https://img.shields.io/badge/Amp-005AF0?style=for-the-badge&logo=amp&logoColor=white) ![Rss](https://img.shields.io/badge/rss-F88900?style=for-the-badge&logo=rss&logoColor=white) 

# Django AMP Blog
Halaman website Regi Apriandi termasuk halaman blog dan resume yang dibagun menggunakan framework Django.

## Docker Compose
```
sudo docker compose up -d
```

## Build Docker Images
```
sudo docker build -t bismillah-webregi-v2-final-deploykube .
sudo docker tag bismillah-webregi-v2-final-deploykube:latest regiapriandi012/bismillah-webregi-v2-final-deploykube:latest
sudo docker push regiapriandi012/bismillah-webregi-v2-final-deploykube:latest
```

## Deploy Kubernetes
### Deployments
```
kubectl create -f postgres-deployment.yaml
kubectl create -f webregi-deployment.yaml
```
### Services
```
kubectl create -f postgres-service.yaml
kubectl create -f webregi-service-nodeport.yaml # for Ingress
kubectl create -f webregi-service-loadbalancer.yaml # for LoadBalancer
```
### Jobs
```
kubectl create -f webregi-job-migrate.yaml
kubectl create -f webregi-job-collectstatic.yaml
```
### Scale Deployment
```
kubectl scale deployment webregi-v2-app --replicas=3
```
### Ingress
```
kubectl create -f webregi-ingress.yaml
```
## Configure Postgresql
```
python manage.py sqlsequencereset webregi
```
```
BEGIN;
SELECT setval(pg_get_serial_sequence('"webregi_post"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "webregi_post";
SELECT setval(pg_get_serial_sequence('"webregi_comment"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "webregi_comment";
SELECT setval(pg_get_serial_sequence('"webregi_photography"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "webregi_photography";
SELECT setval(pg_get_serial_sequence('"webregi_award"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "webregi_award";
SELECT setval(pg_get_serial_sequence('"webregi_certification"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "webregi_certification";
SELECT setval(pg_get_serial_sequence('"webregi_project"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "webregi_project";
SELECT setval(pg_get_serial_sequence('"webregi_publication"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "webregi_publication";
SELECT setval(pg_get_serial_sequence('"webregi_programing"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "webregi_programing";
COMMIT;
```
