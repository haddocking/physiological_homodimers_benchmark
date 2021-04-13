#!/bin/csh
#
foreach i ($argv)
  set fname=`basename $i:r`
  set chainA=A
  set chainB=B
  echo $fname $chainA $chainB
  python ~/haddock_git/pdb-tools/pdbtools/pdb_selaltloc.py $i > tmp1
  python ~/haddock_git/pdb-tools/pdbtools/pdb_delinsertion.py tmp1 > tmpp
  foreach j (HOH GPS GOL ACT SAH SAM 9HJ NAP BB2 SO4 PO4 ACT NAD PHD 1PM NAG ATF HEM PCA VO3 PLP BLM SUC SAM FMA LLP NDP MDP AD3 OAP DED AOX FMN GEL CSO GTX ASB CBD DQN PRL CME TAR SRT DES UNX TMP CMU MMA GTS DOQ UMP SO3 MES LAT PPS MRD SF4 ASJ IPA NO ADP CSD GD3 FAD CIT AIS H3S IOD MPD FES MAL BME BMA VXA ACY 3SL ACP ATP CAZ CSS ISP PB5 CSX YT3 NH4 PT CTE MPO DPR 6CW EPE IMP DGL PYR SAL SP3 OCS A3P PCI EDO ETM BCH BUA P6G SNN FLC AZI DGL SCN MLY GDP CMP DTT FMT ETX IBM OHI TYD POP MRE ALY TAM C2F AKG AMP BOG SIN MLT PE5 SDP FEO CE9 PEG KDO P4C TRS PGE 4OA COA PG6 UNL PG4 P8D TLA IMD DMS EMC Z99 NUP KCX 5GP OXL CAC A8S LBV 12P STR CPS IUM A12 OSE 1C9 DOG AZ4 1QK 6NA D5X BEF BP7 2OY 2QE 2LT 1SY UDP U5P CMK ADE SG8 3MJ 3SM 40F M40 NCD 4QT UPG PPV GSH 1PG 5HF HSA 12P ZHB 6MS 2BA WYD MMV SSI BCT RM4 F6P T3P PG5 GNP MLA TPP 7LL 7HE RCO 7XO MLI THH OAA 36J MLI 40H BQA NLG )
     grep -v $j tmpp >tmp
     \mv tmp tmpp 
  end
  pdb_selchain -$chainA tmpp | pdb_chain -A | pdb_chainxseg | sed -e 's/HETATM/ATOM\ \ /g' |grep ATOM > tmp.out
  echo TER >> tmp.out
  pdb_selchain -$chainB tmpp | pdb_chain -B | pdb_chainxseg | sed -e 's/HETATM/ATOM\ \ /g' |grep ATOM >> tmp.out
  echo END >> tmp.out
  cat tmp.out |\
    sed -e 's/K     K/K+1  K1/g' |\
    sed -e 's/FE    FE/FE+2 FE2/g' |\
    sed -e 's/BR    BR/BR-1 BR1/g' |\
    sed -e 's/CU    CU/CU+2 CU2/g' |\
    sed -e 's/CA    CA/CA+2 CA2/g' |\
    sed -e 's/NI    NI/NI+2 NI2/g' |\
    sed -e 's/MG    MG/MG+2 MG2/g' |\
    sed -e 's/MN    MN/MN+2 MN2/g' |\
    sed -e 's/ZN    ZN/ZN+2 ZN2/g' |\
    sed -e 's/CL    CL/CL-1 CL1/g' > `basename $i`
  \rm tmpp tmp1 tmp.out
end
