#!/bin/bash

# Install the Build and Test Dependencies

apt update
apt install -y curl build-essential tcl

# Download and Extract the Source Code
curl -O http://download.redis.io/redis-stable.tar.gz
tar xzvf redis-stable.tar.gz
cd redis-stable

# Build and Install Redis
make
make test
make install

cd ..

# Configure Redis
mkdir -p /etc/redis
cp redis.conf /etc/redis

# Create a Redis systemd Unit File
cp redis.service /etc/systemd/system/

# Start Redis
systemctl start redis

# Enable Redis to Start at Boot
systemctl enable redis

# Clean
rm -rf redis-stable/
rm redis-stable.tar.gz
