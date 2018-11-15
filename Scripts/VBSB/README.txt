VBSB ver.0.9c
VectorBase Synteny Builder

Exports genes data from http://biomart.vectorbase.org/biomart/, cleans data, converts it to k-way format and then
runs GRIMM-Synteny algorithm to get a series of syntenic blocks for specified species

Requirements:
Unix-based OS, Python v.3.x.x, GRIMM-Synteny v2.02

Installation:
Download GRIMM-Synteny 2.02 from: http://grimm.ucsd.edu/DIST/ and follow instructions in README file. After installation
put 'grimm_synt' executable in environment variable.
Type in cmd: pip3 install *path to setup.py* add *--upgrade* if early version have been installed earlier, for example:
pip3 install C:/Downloads/coursepaper-master/Scripts/VBSB/ --upgrade
make sure pip3 is in environment variable

Usage:
You can use any number of species presented in VectorBase Biomart Genes database. But it is reasonable to use not too many
of ones, because GRIMM-Synteny poorly handles many species research.
Type in cmd: VBSB *1st letter of genus then species, like 'agambiae' or 'hsapiens'* *path to output folder*, for example:
VBSB agambiae aatroparvus aalbimanus C:\output\
