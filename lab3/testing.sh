
TEST()
{
	dir="$1"
	tmpdir=sdbajsd

	./keygen -t rsa -r grace -pub rsaPub -priv rsaPriv
	./keygen -r ec -r grace -pub ecPub -priv ecPriv 

	cp -r "$dir" $tmpdir
	
	./lock -d "$dir" -p rsaPub -r ecPriv -s grace
	
	output=`diff -rq "$dir" $tmpdir`
	
	if [ -z "$output" ]; then 
		echo "lock did not work"
	fi
	./unlock -d "$dir" -p ecPub -r rsaPriv -s grace
	
	output=`diff -rq "$dir" $tmpdir`

	if [ ! -z "$output" ]; then
		echo "dir did not match"
		# exit
	fi

	rm -rf $tmpdir rsaPub rsaPriv ecPub ecPriv
}

# TEST "out_most/Lecture note"

if [ $# -ne 1 ]; then
	echo "sh ./testing.sh <dir>"
	echo "dir:	An outer most directory"
	echo "	It will run keygen, lock, and unlock on all the subdirectories in <dir>"
	echo "	So you want to make sure that there isn't anything that is not a directory in <dir>"
	exit 0
fi

path=$1
for dir in $path/*; do 
	echo "$dir"
	TEST "$dir"
done