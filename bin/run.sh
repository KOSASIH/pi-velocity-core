#!/bin/bash

# Start the Pi-Velocity application
python3 bin/app.py &

# Start the Pi-Velocity web interface
cd web
nginx -g "daemon off;"
