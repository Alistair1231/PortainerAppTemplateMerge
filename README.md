# PortainerAppTemplateMerge
Merges templates and serves them

By default it merges  
https://raw.githubusercontent.com/xneo1/portainer_templates/master/Template/template.json  
and  
https://raw.githubusercontent.com/portainer/templates/master/templates-2.0.json  

Updates once a day automatically.

## Setup

```
git clone https://github.com/Alistair1231/PortainerAppTemplateMerge/
cd PortainerAppTemplateMerge
docker-compose up --build -d
```
 
Now you can access the JSON on http://localhost:8008/combined.json

In the Portainer application settings now add this URL for App Templates http://host.docker.internal:8008/combined.json
