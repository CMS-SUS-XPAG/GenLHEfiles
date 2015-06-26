#!/bin/bash

# grid proxy existence & expiration check
PCHECK=`voms-proxy-info -timeleft`
if [[ ($? -ne 0) || ("$PCHECK" -eq 0) ]]; then
  voms-proxy-init -voms cms --valid 168:00
fi
