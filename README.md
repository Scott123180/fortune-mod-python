# fortune-mod-python

The Fortune-mod program is a simple command-line tool that displays random fortunes from a collection of fortune files. 
It allows you to get a fortune from non-offensive sources (offensive fortunes can easily be added in via modification of the code 
and sourcing it from the original repo.

## Requirements

- Python 3.x

## Installation

1. Clone the repository or download the source code.

```shell
git clone <repository_url>
```

2. Navigate to the project directory.
cd fortune-mod-program

## Usage
```shell
python3 main.py
```

I recommend you hook it into cowsay and add it to your `.zshrc` or `.bashrc` file so that you get a new fortune every time you start your terminal:
```shell
...
...
alias fortune='python3 <path_to_directory>/main.py'
fortune | cowsay
```
