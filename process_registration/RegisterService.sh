#!/bin/bash

# ========================================
# Do some admin to prepare service files
# ========================================

# Read in first argument and store as process name
process_name="$1"
# Copy the .service file with the name of variable above.service
cp template.service "$process_name.service"
# Replace all instances of {Name} with the variable in the newly written file
sed -i "s/{Name}/$process_name/g" "$process_name.service"

# ========================================
# Add supporting files to correct location
# ========================================

# Create directory in /opt if it doesn't exist
mkdir -p "/opt/$process_name"
# Move the new service file to /opt/{process_name}
mv "$process_name.service" "/opt/$process_name/"
# Move binary named {process_name} to /opt/{process_name}
mv "$process_name" "/opt/$process_name/"
# Move config file into the same location
mv "Config.json" "/opt/$process_name/"
# Change permissions of this binary to +wrx
chmod +wrx "/opt/$process_name/$process_name"

# ========================================
# Now start the service
# ========================================

# Register the service
systemctl daemon-reload
# Enable the service
systemctl enable "$process_name.service"
# Reload the service
systemctl reload "$process_name.service"
# Start the service
systemctl start "$process_name.service"
