#!/bin/sh

### Create cards for all mass points

for MNLSP in {100..1300..25}; do
    source writecards_SMS-TChiSlepSnu.sh $MNLSP
done
