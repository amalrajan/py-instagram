# Pystagram
_A python tool to download pictures from Instagram_

## Description

Use this tool to download any picture from Instagram, in the maximum possible resolution. Supports downloading multiple pictures. Paste the links into a text file and pass them into the command line.


## Installation

You need to have Python 3x installed for this to work.

### Windows
```
cd folder_name 
git clone https://github.com/lollichop/Pystagram.git
cd Pystagram
py -3.6 main.py
```

### Linux
```
cd folder_name
git clone https://github.com/lollichop/Pystagram.git
cd Pystagram
python3 main.py
```

## Usage

```
usage: main.py [-h] [-o OUTPUT] type url

positional arguments:
  type                        single / multiple
  url                         url / path to text file

optional arguments:
  -h, --help                  show this help message and exit
  -o OUTPUT, --output OUTPUT  output destination
```

## License
`GNU General Public License v3.0`
