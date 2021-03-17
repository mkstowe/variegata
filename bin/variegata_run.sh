#!/bin/bash
# variegata_run

# Stop on errors
# See https://vaneyckt.io/posts/safer_bash_scripts_with_set_euxo_pipefail/
set -Eeuo pipefail

if [ $# -eq 1 ]; then
	if [ "$1" = "kill" ]; then
		sudo kill -9 "$(sudo lsof -t -i:8000)"
		exit 0
	fi
fi

export FLASK_ENV=development
export FLASK_APP=variegata
flask run --host 0.0.0.0 --port 8000