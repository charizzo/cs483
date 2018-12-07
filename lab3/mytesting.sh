#!/bin/sh


dir=$1
count=0
while [ $count -lt 50 ]
do
	./keygen -t rsa -r grace -pub rsaPub -priv rsaPriv
	./keygen -r ec -r grace -pub ecPub -priv ecPriv

	./lock -d "$dir" -p rsaPub -r ecPriv -s grace

	./unlock -d "$dir" -p ecPub -r rsaPriv -s grace

	rm  rsaPub rsaPriv ecPub ecPriv
	((count++))
	echo $count
done
