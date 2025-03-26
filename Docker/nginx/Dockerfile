# Use Ubuntu as the base image
FROM ubuntu

# Update package lists to get the latest versions
RUN apt update

# Install curl (a command-line tool for making HTTP requests)
RUN apt-get install -y curl

# Download and execute the Node.js setup script to add Node.js repository
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -

# Upgrade all installed packages to the latest versions
RUN apt-get upgrade -y

# Install Node.js and npm (Node Package Manager)
RUN apt-get install -y nodejs

# Copy necessary files for the Node.js application into the container
COPY package.json package.json
COPY package-lock.json package-lock.json
COPY server.js server.js

# Install project dependencies defined in package.json
RUN npm install

# Set the default command to run the Node.js server when the container starts
ENTRYPOINT ["node", "server.js"]
