#!/bin/bash
# insta485db

# Stop on errors
# See https://vaneyckt.io/posts/safer_bash_scripts_with_set_euxo_pipefail/
set -Eeuo pipefail

# Sanity check command line options
usage() {
  echo "Usage: $0 (create|destroy|reset|dump)"
}

if [ $# -ne 1 ]; then
  usage
  exit 1
fi

root="$(dirname "$(dirname "$(realpath "$0")")")"
data_dir="$root/variegata/data"

# Parse argument.  $1 is the first argument
case $1 in
  "create")
    if [ -f "$data_dir/variegata.sqlite3" ]; then
      echo "Error: database already exists"
      exit 1
    fi

    sqlite3 "$data_dir"/variegata.sqlite3 < "$root"/sql/schema.sql
    sqlite3 "$data_dir"/variegata.sqlite3 < "$root"/sql/data.sql
    ;;

  "destroy")
    rm -rf "$data_dir"/variegata.sqlite3
    ;;

  "reset")
    rm -rf "$data_dir"/variegata.sqlite3
    sqlite3 "$data_dir"/variegata.sqlite3 < "$root"/sql/schema.sql
    sqlite3 "$data_dir"/variegata.sqlite3 < "$root"/sql/data.sql
    ;;

  "dump")
  	printf "Events:\n\n"
    sqlite3 -batch -line "$data_dir"/variegata.sqlite3 'SELECT * FROM events'
    ;;

  *)
    usage
    exit 1
    ;;
esac