sudo apt-get update
sudo apt-get -y install apache2

# below is instruction for apache + ubuntu 18.04 by certbot

sudo apt-get -y install software-properties-common
sudo add-apt-repository -y universe
sudo add-apt-repository -y ppa:certbot/certbot
sudo apt-get update
sudo apt-get -y install certbot python-certbot-apache 

sudo certbot --apache