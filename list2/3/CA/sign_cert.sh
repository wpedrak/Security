#!/bin/bash

openssl genrsa -out ca.key 2048
openssl req -new -x509 -key ca.key -out ca.crt # generate self signed certificate
openssl x509 -req -in example.org.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out example.org.crt #sign
