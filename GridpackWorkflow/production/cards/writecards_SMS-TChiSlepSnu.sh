#!/bin/sh

### Use the templates to create cards for a specific mass point

MNLSP=$1

mkdir -p SMS-TChiSlepSnu_mChi-${MNLSP}
cp SMS-TChiSlepSnu_run_card.dat SMS-TChiSlepSnu_mChi-${MNLSP}/SMS-TChiSlepSnu_mChi-${MNLSP}_run_card.dat
sed "s/%MNLSP%/${MNLSP}/g" SMS-TChiSlepSnu_proc_card.dat > SMS-TChiSlepSnu_mChi-${MNLSP}/SMS-TChiSlepSnu_mChi-${MNLSP}_proc_card.dat
sed "s/%MNLSP%/${MNLSP}/g" SMS-TChiSlepSnu_customizecards.dat > SMS-TChiSlepSnu_mChi-${MNLSP}/SMS-TChiSlepSnu_mChi-${MNLSP}_customizecards.dat
