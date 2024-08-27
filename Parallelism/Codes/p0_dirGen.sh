#!/bin/bash

#These commands create the working directories

javac CalculateRunner_V2.java
javac CalculateCosine_V2.java

mkdir FullPDB
mkdir FullPDB/sized7Lat
mkdir FullPDB/sized7NoLat
mkdir FullPDB/sized8NoLat
mkdir FullPDB/sized8Lat

mkdir FullPDB/sized7Lat/Interacting
mkdir FullPDB/sized7NoLat/Interacting
mkdir FullPDB/sized8Lat/Interacting
mkdir FullPDB/sized8NoLat/Interacting

mkdir FullPDB/sized7Lat/NonInteracting
mkdir FullPDB/sized7NoLat/NonInteracting
mkdir FullPDB/sized8Lat/NonInteracting
mkdir FullPDB/sized8NoLat/NonInteracting

mkdir AlphaFold
mkdir AlphaFold/sized7Lat
mkdir AlphaFold/sized7NoLat
mkdir AlphaFold/sized8NoLat
mkdir AlphaFold/sized8Lat

mkdir AlphaFold/sized7Lat/Interacting
mkdir AlphaFold/sized7NoLat/Interacting
mkdir AlphaFold/sized8Lat/Interacting
mkdir AlphaFold/sized8NoLat/Interacting

mkdir AlphaFold/sized7Lat/NonInteracting
mkdir AlphaFold/sized7NoLat/NonInteracting
mkdir AlphaFold/sized8Lat/NonInteracting
mkdir AlphaFold/sized8NoLat/NonInteracting


mkdir Experimental
mkdir Experimental/sized7Lat
mkdir Experimental/sized7NoLat
mkdir Experimental/sized8NoLat
mkdir Experimental/sized8Lat

mkdir Experimental/sized7Lat/Interacting
mkdir Experimental/sized7NoLat/Interacting
mkdir Experimental/sized8Lat/Interacting
mkdir Experimental/sized8NoLat/Interacting

mkdir Experimental/sized7Lat/NonInteracting
mkdir Experimental/sized7NoLat/NonInteracting
mkdir Experimental/sized8Lat/NonInteracting
mkdir Experimental/sized8NoLat/NonInteracting
