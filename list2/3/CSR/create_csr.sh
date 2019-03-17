#!/bin/bash

openssl genrsa -out example.org.key 2048
openssl req -new -key example.org.key -out example.org.csr
# some questions
# result in example.org.csr