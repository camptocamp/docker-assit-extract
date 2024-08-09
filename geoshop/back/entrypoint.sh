#!/bin/bash
set -euo pipefail

cd /geoshop/geoshop-back

if [[ "$( python3 manage.py showmigrations | grep '\[ \]' )" != "" ]]; then
    python3 manage.py migrate --noinput
else
    echo "No pending migrations"
fi

if [[ ! -f "/geoshop/.fixtures_lock" ]]; then
    python3 manage.py fixturize
    if [[ $? == 0 ]]; then 
      touch "/geoshop/.fixtures_lock" 
    fi
else
    echo "No fixturizing needed."
fi

if [[ ! -f "/geoshop/.sampledata_lock" ]]; then
    # TODO: Pass host, password and dbname from the env section of the postgis
    # FIXME use enviromnet variales if possible
    PGPASSWORD=geoshop psql --host=postgis --username=geoshop --dbname=geoshop -p 5432 < /geoshop/sampledata.sql
    touch "/geoshop/.sampledata_lock"
fi

python3 manage.py collectstatic --noinput
python3 manage.py runserver 0.0.0.0:8000
