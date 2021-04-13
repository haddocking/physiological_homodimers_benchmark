#!/bin/csh
#
source /home/abonvin/haddock2.4/haddock_configure.csh
set cnsExec="/home/software/science/cns/cns_solve_1.31-UU/intel-x86_64bit-linux/bin/cns"
set outfile="scoring.out"

$cnsExec < scoring.inp > $outfile
gzip -f $outfile
