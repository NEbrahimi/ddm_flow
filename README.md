# ddm-flow

`ddm-flow` is a toolset designed for processing, organizing, and visualizing data for individual FoVs from DDm analysis. This repository provides all the necessary scripts and instructions to get started.

## Installation

### From PyPi

You can easily install `ddm-flow` from PyPi:

```
pip install ddm-flow==0.1.1
```

### From Source

Clone the repository and navigate to its directory:

[```]
git clone https://github.com/NEbrahimi/ddm-flow.git
cd ddm-flow
[```]

Install using pip:

[```]
pip install .
[```]

## Usage

After installation, you can use the provided scripts anywhere from the command line. Here's a brief overview:

### multisheet_aggregator

Use the `multisheet_aggregator` command followed by the path to the directory you want to process. The `-o` flag allows you to specify an output filename:

[```]
multisheet_aggregator <path_to_directory> -o <output_filename>
[```]

Replace `<path_to_directory>` with the actual path to your directory and `<output_filename>` with your desired output file name.

### csv_organizer

Use the `csv_organizer` command followed by the path to the directory you want to process:

[```]
csv_organizer <path_to_directory>
[```]

Replace `<path_to_directory>` with the actual path to your directory.

### plotter

Use the `plotter` command followed by the path to the directory you want to process:

[```]
plotter <path_to_directory>
[```]

Replace `<path_to_directory>` with the actual path to your directory.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
