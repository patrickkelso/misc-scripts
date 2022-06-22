#!/bin/bash
# Trust me this solves a problem.
# Correlating account IDs from multiple files into a CSV for accounts Payable.

set -euo pipefail

ACCOUNTLIST="accounts"
CREDITLIST="credits.csv"
INVOICELIST="billingreport.csv"

for i in `cat $ACCOUNTLIST`; do
	if `grep -q $i $CREDITLIST`
	then
		INVOICENUM=`grep $i $CREDITLIST | awk -F "," '{print $3}'`
		CREDITVAL=`grep $i $CREDITLIST | awk -F "," '{print $4}'`
		INVOICELINE=`grep $i $INVOICELIST` 
		echo  $INVOICENUM','$CREDITVAL","$INVOICELINE
	else
		INVOICENUM='No Invoice'
		CREDITVAL='No Credit'
		INVOICELINE=`grep $i $INVOICELIST` 
		echo  $INVOICENUM','$CREDITVAL","$INVOICELINE
	fi
done
