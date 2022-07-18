server {
    listen 80;
    server_name 104.248.19.175;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/sammy/myproject;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/root/projectGrupepe.sock;
    }
}