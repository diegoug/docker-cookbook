#!/bin/bash

__start_nodeinspector() {
forever start /usr/local/bin/node-inspector --web-port=8081
}

__debugger_server() {
cd /opt/nodejs/
NODE_ENV=development supervisor --debug server.js
}

# Call all functions
__start_nodeinspector
__debugger_server
