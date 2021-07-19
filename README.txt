This docker-compose setup creates four web services, with the virtual hostnames service_a.local, service_b.local, foo.local, and bar.local. It also creates an nginx-proxy container, based on the jwilder/nginx-proxy Docker image, that serves as a reverse proxy to direct requests to the correct service, based on hostname. nginx-proxy expects each service to have the VIRTUAL_HOSTNAME environment variable set. 

service_a.local and service_b.local run on the webnet virtual network. foo.local and bar.local run on the webnet2 virtual network. These services do not expose any ports to the host computer. nginx-proxy runs on both virtual networks and has port 80 exposed.

To handle domain name resolution, I added the following line to my local /etc/hosts file:
127.0.0.1 service_a.local service_b.local foo.local bar.local

When the containers are running, I can enter http://service_a.local in my browser, and the request will go to port 80 and be directed to the service_a container. 

# Sample session using curl, with the virtual hostnames in /etc/hosts.
$ curl http://service_a.local
<h3>Hello World from service_a!</h3><b>Hostname:</b> adcdb572fcd0<br/>

$ curl http://foo.local
<h3>Hello World from foo!</h3><b>Hostname:</b> 305fd94759b2<br/>

$ curl http://service_b.local
<h3>Hello World from service_b!</h3><b>Hostname:</b> cad602b36a66<br/>

$ curl http://bar.local
<h3>Hello World from bar!</h3><b>Hostname:</b> 45b50a7951ac<br/>

The four web services all use the flask-service image that I created. This is a simple Flask application that displays a Hello World message based on the the value of the environment variable SERVICE_NAME, which I set for each service in docker-compose.yml. 







