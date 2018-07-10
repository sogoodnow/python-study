worker_processes $worker_processes;
pid        logs/nginx.pid;

events {
    worker_connections  1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile        on;
    keepalive_timeout  65;
    gzip  on;

    server {
        listen       $listen;
        server_name  $server_name;

        location / {
            root   $root;
            index  index.html index.htm;
        }
    }
}