# Git Release Notes

Generate release notes based on git history.

## Getting Started
#### Warning
The Templite engine runs untrusted python code. Please examine template files before using them

### Prerequisites

Python and Git must be installed

### Installing

Clone the repository

```
git clone https://github.com/iangorse/GRN.git
```

Change to the directory

```
cd GRN
```

### Usage

```
python grn.py --help

usage: grn.py [-h] [--gitdir GITDIR] [--output OUTPUT] template

positional arguments:
  template         the template file to use

optional arguments:
  -h, --help       show this help message and exit
  --gitdir GITDIR  the git repository path to build release notes against
  --output OUTPUT  outputs results to a filename
```

#### Examples

##### Warning
The Templite engine runs untrusted python code. Please examine template files before using them

Build a markdown representation of the git log

```
python grn.py markdown
```

Build a HTML represenation of a git log of a different repository
```
python grn.py html --gitdir "c:\another repo\.git"
```


## Built With

* [Python 3.6](https://www.python.org/) - Python
* [Templite](http://code.activestate.com/recipes/496702/) - Simple Template Engine for Python



## Authors

* **Ian Gorse** - *Initial work* - [Ian Gorse](https://github.com/iangorse)

## Acknowledgments

This project was inspired by https://github.com/ariatemplates/git-release-notes




