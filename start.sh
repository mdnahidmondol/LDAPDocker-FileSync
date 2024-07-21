#!/bin/bash

# Mount NFS share
mount -t nfs host.docker.internal:/nfs_share /data

# Run permission sync
python3 ldap_acl.py

# Start the main application
python3 app.py