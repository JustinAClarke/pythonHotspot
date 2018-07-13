FROM resin/raspberry-pi-debian

# install required packages
RUN apt-get update && apt-get install -yq --no-install-recommends \
    wireless-tools hostapd dnsmasq \
    network-manager \
    python3-pip \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# define our working directory in the container
WORKDIR usr/src/app

# copy all files in our root to the working directory
COPY . ./

RUN pip3 install -r requirements.txt --extra-index-url https://www.piwheels.org/simple

# enable systemd init system in the container
ENV INITSYSTEM on

# app.py will run when the container starts up on the device
CMD ["python3", "app.py"]


