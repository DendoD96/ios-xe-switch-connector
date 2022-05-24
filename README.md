# IOS-XE Switch Connector

## Overview
This is a stub for Cisco IOS-XE Switch Connector.

## Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m ios_xe_switch_connector
```

and open your browser to here:

```
http://localhost:8080/ui/
```

Your Swagger definition lives here:

```
http://localhost:8080/swagger.json
```

To launch the integration tests, use tox:
```
pip3 install -r test-requirements.txt
tox
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t ios_xe_switch_connector .

# starting up a container
docker run -p 8080:8080 ios_xe_switch_connector
```