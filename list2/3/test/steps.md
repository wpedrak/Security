* install nginx
* add **server** section to **http** section in **/etc/nginx/nginx.conf**
  >server {
  >    listen              443 ssl;
  >    server_name         www.kogucik.pl;
  >    ssl_certificate     /home/wojtek/Documents/Semestr10/Security/list2/3/CA/example.org.crt;
  >    ssl_certificate_key /home/wojtek/Documents/Semestr10/Security/list2/3/CSR/example.org.key;
  >    ssl_protocols       TLSv1 TLSv1.1 TLSv1.2;
  >    ssl_ciphers         HIGH:!aNULL:!MD5;
  >}

* chrome says that certificate is not trusted
What can be done? 
One can edit chrome settings or become trusted CA