"""
Fixel Sampling Utility

This script computes the mean values from sampled fixel data, 
ignoring zero values in the calculation.

Usage:
    python fixelsampling.py <input_file> <output_file>
"""

import argparse
import numpy as np


def compute_means(input_file, output_file='means.txt'):
    """
    Computes the mean of non-zero fixel data for each track.
    
    Args:
        input_file (str): Path to the input .txt file containing one track per line.
        output_file (str): Path to save the output means.
    """
    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith('#')]

    n_tracks = len(lines)
    means = np.zeros((n_tracks, 1))

    for i, line in enumerate(lines):
        data = np.array([float(x) for x in line.split()])
        nonzero_data = data[data != 0]
        mean = np.mean(nonzero_data) if nonzero_data.size > 0 else 0.0
        means[i, 0] = mean

    np.savetxt(output_file, means, fmt='%.6f')
    print(f"Saved mean values to: {output_file}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Compute mean values from sampled fixel data.")
    parser.add_argument('input', help="Path to input .txt file (one line per track)")
    parser.add_argument('output', help="Output file name")

    args = parser.parse_args()

    compute_means(args.input, args.output)
