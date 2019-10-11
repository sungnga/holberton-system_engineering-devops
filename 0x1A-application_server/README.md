# 0x1A. Application server

<p>
<img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/9/c7d1ed0a2e10d1b4e9b3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUXW7JF5MT%2F20191010%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20191010T223910Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1b7b3ef2a6c0355a8f259bc02161b3d8aba6997b198a9277103ec48358d9802c">
</p>

## Background Context
Your web infrastructure is already serving web pages via Nginx that you installed in your first web stack project. While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your Nginx and make is serve your Airbnb clone project.

## Resources
* [Application server vs web server](https://www.nginx.com/resources/glossary/application-server-vs-web-server/)
* [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04) (As mentioned in the video, do **not** install Gunicorn using `virtualenv`, just install everything globally)
* [Running Gunicorn](http://docs.gunicorn.org/en/latest/run.html)
* [Be careful with the way Flask manages slash](https://werkzeug.palletsprojects.com/en/0.14.x/routing/) in [route](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.route) - `strict_slashes`
* [Upstart documentation](http://upstart.ubuntu.com/cookbook/)

