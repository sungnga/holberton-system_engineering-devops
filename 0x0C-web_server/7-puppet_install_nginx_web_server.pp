# A Puppet script to configure the Nginx server
exec {'/usr/bin/env apt-get update':}
exec {'/usr/bin/env apt-get -y install nginx':}
exec {'/usr/bin/env ufw allow "Nginx HTTP"':}
exec {'/usr/bin/env echo "Holberton School" > /var/www/html/index.nginx-debian.html':}
exec {'/usr/bin/env sed -i "/listen 80 default_server/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default':}
exec {'/usr/bin/env service nginx start':}
