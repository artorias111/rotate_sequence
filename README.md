# Rotate your sequence

A script to take a single fasta sequence, and rotate it at a position of your choice. 

By default, the script gives one output to stdout with a space at the position of the roate site in the fasta sequence for visual inspection. This is directed to `stderr`, and can be safely ignored post inspection. 

## Usage
```shell
# save the rotated file by redirecting stdout
python3 rotate_ref.py --ref /path/to/mt/genome.fa --pos 3986 > rotated_sequence.fa

# if, for some reason, you want to save the rotated site to a file
python3 rotate_ref.py --ref /path/to/mt/genome.fa --pos 3986 > rotated_sequence.fa 2> rotated_sequence_inspection.txt
```
