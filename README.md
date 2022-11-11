![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![Amp](https://img.shields.io/badge/Amp-005AF0?style=for-the-badge&logo=amp&logoColor=white) ![Rss](https://img.shields.io/badge/rss-F88900?style=for-the-badge&logo=rss&logoColor=white) 

![](https://github.com/regiapriandi012/blog-amp-django/actions/workflows/codeql.yml/badge.svg)
![](https://github.com/regiapriandi012/blog-amp-django/actions/workflows/dependency-review.yml/badge.svg)
![](https://github.com/regiapriandi012/blog-amp-django/actions/workflows/django.yml/badge.svg)
![](https://github.com/regiapriandi012/blog-amp-django/actions/workflows/docker-image.yml/badge.svg)

# Django AMP Blog
Django blog application built with AMP technology to speed up loading on mobile browsers. This blog application is integrated with django-summernote technology where this technology makes it easy to write blogs on the django admin admin page. This application has also built an RSS feed which is very much needed on a blog.

## Features
- ### Django-Summernote
  This feature makes it very easy to write blogs in the application.
  
  <img width="700" alt="image" src="https://user-images.githubusercontent.com/69528812/201313939-31af9d95-5d04-464d-a78c-626c5e084167.png">
- ### AMP Technology
  this technology can speed up the process of loading applications on mobile browsers.

  <img width="700" alt="image" src="https://user-images.githubusercontent.com/69528812/201315817-ce8889eb-a947-4b80-b19b-3cbf6cfaddab.png">
- ### RSS Feeds
  Useful for spreading the latest blog content.
  
  <img width="700" alt="image" src="https://user-images.githubusercontent.com/69528812/201314545-1d836c0c-f9a4-4350-882c-f0d936884c42.png">
- ### Sitemap
  Very important to improve the SEO of a blog.
  
  <img width="700" alt="image" src="https://user-images.githubusercontent.com/69528812/201314621-68631951-ab09-473a-83b5-0e5155fb8d75.png">
# 
## App Looks
### Blog Home
<img width="941" alt="image" src="https://user-images.githubusercontent.com/69528812/201320642-ef40f33b-458a-4f4f-92d1-b14a43bebecc.png">

### Blog Detail
<img width="946" alt="image" src="https://user-images.githubusercontent.com/69528812/201320818-fa5550b6-c735-4852-8ecd-a9eaa05bc59e.png">

#
# Build the App
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
## Configure Postgresql (optional)
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
