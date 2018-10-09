#!/bin/bash

HTTP_CODE=$(curl -s -o /dev/null -w '%{http_code}' $1)

if [ "$HTTP_CODE" -eq '200' ]; then
  exit 0;
fi

echo "Wrong HTTP_CODE: ${HTTP_CODE} != 200"

exit 1
