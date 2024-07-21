#!/bin/bash

# Install NFS server
sudo apt-get update
sudo apt-get install -y nfs-kernel-server

# Create shared directory
sudo mkdir -p /nfs_share
sudo chown nobody:nogroup /nfs_share
sudo chmod 777 /nfs_share

# Configure NFS export
echo "/nfs_share *(rw,sync,no_subtree_check,no_root_squash)" | sudo tee -a /etc/exports

# Apply changes and restart NFS server
sudo exportfs -a
sudo systemctl restart nfs-kernel-server