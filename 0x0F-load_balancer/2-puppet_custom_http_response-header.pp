# A Puppet script that configures the Nginx so that its HTTP response contains a custom header
exec {'/usr/bin/env apt-get update':}
exec {'/usr/bin/env apt-get -y install nginx':}
exec {'/usr/bin/env ufw allow "Nginx HTTP"':}
exec {'/usr/bin/env echo "Holberton School" > /var/www/html/index.nginx-debian.html':}
exec {'/usr/bin/env echo "Ceci n\'est pas une page" > /usr/share/nginx/html/custom_404.html':}
exec {'/usr/bin/env sed -i "/listen 80 default_server/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default':}
exec {'/usr/bin/env sed -i "/listen 80 default_server/a error_page 404 /custom_404.html;location = /custom_404.html {root /usr/share/nginx/html;internal;}" /etc/nginx/sites-available/default':}
exec {'/usr/bin/env sed -i "/listen 80 default_server/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default':}
exec {'/usr/bin/env service nginx restart':}
