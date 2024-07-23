#!/bin/bash
set -euo pipefail

psql --host=$PGHOST --username=$PGUSER --dbname=$PGDB \
  < /updatedb/001_update_db.sql  \
  < /updatedb/002_create_test_data.sql \
  < /updatedb/003_system_config.sql