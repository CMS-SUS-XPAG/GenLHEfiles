#!/bin/bash

FILEDIR=$1
PROCNAME=$2

for FILE in `ls /eos/uscms/store/user/pedrok/${FILEDIR}/${PROCNAME}*undecayed*`
  do
    xrdcp ... lhe/
  done

# add some command line options?
python create_update_header_config.py
python update_header.py myconfig.cfg

for FILE in `ls lhe_processed/${PROCNAME}*`
  do
    xrdcp ${FILE} ...
  done
