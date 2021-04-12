if [ "$#" != 1 ]; then
    echo "Usage: ${0##*/} PDB_list"
    exit 1
fi

while read -r line
do
    name=`echo $line | awk '{print $1}'`

    if [ ! -f "${name}.hdf5" ]; then
	python generate_grids.py ${name}/pdb ${name}/pssm ${name}.hdf5 
    fi

done < $1
