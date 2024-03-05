# Linux_Installer

This repo provides one with the ability to install a set of Sense-Scape releases.
Upon completetion, the software should be running in a docker container on ones pc.

A sensor may send data to it via exposed ports or one may configure simulators to run within the container itself.

## Installation Procedure

### Aquiring Install Components:

- Clone this repo
- Specify the component versions one wishes to use in the `Install.json` (note: older release versions may not follow correct naming convention. version 2+ is guarenteed to work)
- run `python3 DownloadGithubRelease` to install all components
- navigate into the `Install` folder to find all components
- These may be run on a local linux machine but there is no gaurentee that they shall work
- The intention is to run them in a Docker container


### Configuring Docker

- There should be a SensorDockerFile shipped on clone
- Docker is therefore required

#### Configuring Storage Locations

- The system shall have the ability to write wav files to storage
- as such create a docker volume using `docker volume create WAVData`
- note that `WAVData` is just a name and one may change it - the docker file should also be changed in this case
- If one has defined a non standard volume name then open the docker file and change the moounted volume name

#### Exposing Ports

- The ports should already be exposed so one should have to do no configuration of this
- ports 10000 to 10100 should be exposed - there is no guarentee I keep this up to date
- These are exposed as there is a handshake between sensor and server to be allocated a port
- This may change in the future but I do not expect it to  

#### Configuring Sensor Software

- The sensor software shoould generally come preconfigured with standard ports
- As such do not change any ports or IP information
- If you really want knock yourself out but I shall not be responsible for the hours of therapy that shall be required

## Running the Software

- To build the docker container run `sudo docker build -f <Docker File Name> -t <Image Name>`
- todo

## Accessing the Data

- todo

### TODO

- run automatically
- configure sensors remotely - may have to pull sensors into their own images
- 
 
