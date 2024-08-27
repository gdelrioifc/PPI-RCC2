#!/usr/bin/bash

# Here you use CalculateCosine_V2.java to calculate the Angles between pairs of proteins
# if the samples have very large populations
samples=500

condition_=d7Lat_
condition=d7Lat

proc=24 #This is a variable for CalculateCosine_V2 in function of the available processors

loop=$((samples/5-1))
for ((i=0; i<=$loop ;i++))
do
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/full_$condition_$((i*5)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_full_$condition_$((i*5)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/sim_full_$condition_$((i*5)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_sim_full_$condition_$((i*5)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/full_$condition_$((i*5+1)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_full_$condition_$((i*5+1)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/sim_full_$condition_$((i*5+1)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_sim_full_$condition_$((i*5+1)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/full_$condition_$((i*5+2)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_full_$condition_$((i*5+2)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/sim_full_$condition_$((i*5+2)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_sim_full_$condition_$((i*5+2)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/full_$condition_$((i*5+3)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_full_$condition_$((i*5+3)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/sim_full_$condition_$((i*5+3)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_sim_full_$condition_$((i*5+3)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/full_$condition_$((i*5+4)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_full_$condition_$((i*5+4)).txt &
java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/sim_full_$condition_$((i*5+4)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_sim_full_$condition_$((i*5+4)).txt

sleep 3
done

condition_=d7NoLat_
condition=d7NoLat

loop=$((samples/5-1))
for ((i=0; i<=$loop ;i++))
do
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/full_$condition_$((i*5)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_full_$condition_$((i*5)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/sim_full_$condition_$((i*5)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_sim_full_$condition_$((i*5)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/full_$condition_$((i*5+1)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_full_$condition_$((i*5+1)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/sim_full_$condition_$((i*5+1)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_sim_full_$condition_$((i*5+1)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/full_$condition_$((i*5+2)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_full_$condition_$((i*5+2)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/sim_full_$condition_$((i*5+2)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_sim_full_$condition_$((i*5+2)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/full_$condition_$((i*5+3)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_full_$condition_$((i*5+3)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/sim_full_$condition_$((i*5+3)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_sim_full_$condition_$((i*5+3)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/full_$condition_$((i*5+4)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_full_$condition_$((i*5+4)).txt &
java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/sim_full_$condition_$((i*5+4)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_sim_full_$condition_$((i*5+4)).txt

sleep 3
done

condition_=d8Lat_
condition=d8Lat

loop=$((samples/5-1))
for ((i=0; i<=$loop ;i++))
do
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/full_$condition_$((i*5)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_full_$condition_$((i*5)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/sim_full_$condition_$((i*5)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_sim_full_$condition_$((i*5)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/full_$condition_$((i*5+1)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_full_$condition_$((i*5+1)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/sim_full_$condition_$((i*5+1)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_sim_full_$condition_$((i*5+1)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/full_$condition_$((i*5+2)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_full_$condition_$((i*5+2)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/sim_full_$condition_$((i*5+2)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_sim_full_$condition_$((i*5+2)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/full_$condition_$((i*5+3)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_full_$condition_$((i*5+3)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/sim_full_$condition_$((i*5+3)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_sim_full_$condition_$((i*5+3)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/full_$condition_$((i*5+4)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_full_$condition_$((i*5+4)).txt &
java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/sim_full_$condition_$((i*5+4)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_sim_full_$condition_$((i*5+4)).txt

sleep 3
done

condition_=d8NoLat_
condition=d8NoLat

loop=$((samples/5-1))
for ((i=0; i<=$loop ;i++))
do
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/full_$condition_$((i*5)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_full_$condition_$((i*5)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/sim_full_$condition_$((i*5)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_sim_full_$condition_$((i*5)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/full_$condition_$((i*5+1)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_full_$condition_$((i*5+1)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/sim_full_$condition_$((i*5+1)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_sim_full_$condition_$((i*5+1)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/full_$condition_$((i*5+2)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_full_$condition_$((i*5+2)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/sim_full_$condition_$((i*5+2)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_sim_full_$condition_$((i*5+2)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/full_$condition_$((i*5+3)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_full_$condition_$((i*5+3)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/sim_full_$condition_$((i*5+3)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_sim_full_$condition_$((i*5+3)).txt &
nohup java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/full_$condition_$((i*5+4)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_full_$condition_$((i*5+4)).txt &
java -Xmx5G CalculateCosine_V2 FullPDB/size$condition/NonInteracting/sim_full_$condition_$((i*5+4)).txt 359 $proc > FullPDB/size$condition/NonInteracting/AnglesAt_sim_full_$condition_$((i*5+4)).txt

sleep 3
done

