#!/bin/bash -l
#$ -S /bin/bash
#$ -l h_rt=20:00:0
#$ -l memory=16G
#$ -pe mpi 8
#$ -l gpu=2
# Set the name of the job.
#$ -N PlanetExp6
# 4. Request 15 gigabyte of TMPDIR space (default is 10 GB)
#$ -l tmpfs=20G
# 6. Set the working directory to somewhere in your scratch space.  This is
# a necessary step with the upgraded software stack as compute nodes cannot
# write to $HOME.
# Replace "<your_UCL_id>" with your UCL user ID :)
#$ -wd /home/uceshaf/Scratch/outputs/Exp6
#
# 7. Your work *must* be done in $TMPDIR 
cd $TMPDIR
#
# Syed Roshaan Ali Shah
# July 2019
# Initial  computations - script for setting up 
#
start1=$(date +%s.%N)
echo unloadingCompilers
module unload compilers mpi
module load compilers/gnu/4.9.2
module load python3/recommended
module load cuda/8.0.61-patch2/gnu-4.9.2
module load cudnn/6.0/cuda-8.0
module load tensorflow/1.4.1/gpu
end1=$(date +%s.%N)
#
time=$(echo "$end1 - $start1" | bc)
echo $time
#
start2=$(date +%s.%N)
echo pip3s
pip3 install --upgrade pip --user
pip3 install keras --user
#pip3 install tensorflow --user
pip3 install pydot --user
pip3 install matplotlib --user
pip3 install pillow --user
pip3 install sklearn --user
pip3 install --upgrade segmentation-models --user
#pip install --upgrade wandb --user
#wandb login d0b6f9c18e15e74c1a84a181ea6bece64fb937fd
#
$
end2=$(date +%s.%N)
time=$(echo "$end2 - $start2" | bc)
echo $time
#
echo cuda_install
#module load cuda/10.0.130/gnu-4.9.2
#module load cudnn/7.5.0.56/cuda-10.0
#
#
echo cuda_loaded
#
start3=$(date +%s.%N)
#wandb run python3 /home/uceshaf/FinalProject/PlanetExps/Exp6/Exp6.py
python3 /home/uceshaf/FinalProject/PlanetExps/Exp6/Exp6.py
end3=$(date +%s.%N)
#
time=$(echo "$end3 - $start3" | bc)
echo $time


