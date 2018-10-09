#!/bin/bash

./scripts/health_check.sh $1
if [ "$?" -ne 0 ]; then
  exit 1;
fi

python venv.py .venv > /dev/null
. ./.venv/bin/activate > /dev/null
./scripts/most_common_word.py $1
deactivate
