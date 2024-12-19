# RAGAS factual accuracy

A simple script to run factual accuracy using the RAGAS approach.

## Instructions

The *--data* argument in the notebook must point to a file with the following characteristics:
- saved as a JSONL file
- each line of the JSONL file must be the summary that must be evaluated for factual accuracy

The *--sources* argument in the notebook must point to a file with the following characteristics:
- saved as a JSONL file
- each line of the JSONL file must be the source file used to generate the summary

In order to load the model as done in the script you will need to use a powerful GPU. Not all quantization types are supported by all GPUs.
If you are running this example on Colab you will need at least an L4 GPU, the T4 can't run the example model.
