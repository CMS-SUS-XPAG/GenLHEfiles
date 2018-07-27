#!/bin/bash
# Usage: ./copyOldCardsFor2017.sh <old folder name>
# example: ./copyOldCardsFor2017.sh dyellell012j_5f_NLO_FXFX

if [ -z $1 ]; then
    echo "You need to enter the folder name as an argument"
    echo "ex: ./copyOldCardsFor2017.sh dyellell012j_5f_NLO_FXFX"
    exit 1
fi


old_cards_relative_path=$1
absPath=$(pwd)
new_cards_path=${absPath}/${old_cards_relative_path}/templatecards
old_cards_path=${absPath}/${old_cards_relative_path}/templatecards_2016

mv $new_cards_path $old_cards_path
mkdir $new_cards_path
cp $old_cards_path/* $new_cards_path/

for run_card in $(find $new_cards_path -type f -follow -print -name "*run_card*"); do 
    # reweight_PDF may not be present in older cards
    if grep -q -e ".*= *reweight_PDF" $run_card; then
        sed -i "s/^.*= *lhaid/\$DEFAULT_PDF_SETS = lhaid/g" $run_card
        sed -i "s/.*= *reweight_PDF/\$DEFAULT_PDF_MEMBERS = reweight_PDF/g" $run_card
    else
        sed -i "s/^.*= *lhaid/\$DEFAULT_PDF_SETS = lhaid\n\$DEFAULT_PDF_MEMBERS = reweight_PDF/g" $run_card
    fi
    sed -i "s/.*= *PDF_set_min//g" $run_card
    sed -i "s/.*= *PDF_set_max//g" $run_card
done
