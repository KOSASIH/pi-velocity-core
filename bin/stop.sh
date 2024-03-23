#!/bin/bash

# Stop the Pi-Velocity application
pkill -f python3

# Stop the Pi-Velocity web interface
cd web
nginx -s stop
