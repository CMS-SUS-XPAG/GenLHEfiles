#!/bin/bash

# grid proxy existence check
voms-proxy-info --all > /dev/null
if [ $? -ne 0 ]; then
  voms-proxy-init -voms cms --valid 168:00
fi

# grid proxy expiration check
PCHECK=`voms-proxy-info --all | grep "timeleft  : 00:00:00"`
if [ -n "$PCHECK" ]; then
  voms-proxy-init -voms cms --valid 168:00
fi
PCHECK=`voms-proxy-info --all | grep "timeleft  : 0:00:00"`
if [ -n "$PCHECK" ]; then
  voms-proxy-init -voms cms --valid 168:00
fi
