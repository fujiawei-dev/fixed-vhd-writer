# Fixed VHD Writer

## Installation

```shell
pip install -U fixed-vhd-writer
```

```shell
pip install -U fixed-vhd-writer -i https://pypi.douban.com/simple
```

## Usage

```shell
$ vhdwriter --help
Usage: vhdwriter [OPTIONS]

Options:
  -v, --vhd_file TEXT          specify .vhd file to write  [required]
  -b, --bin_file TEXT          specify .bin file to read
  -o, --sector_offset INTEGER  specify sector offset to write
  -s, --show_geometry BOOLEAN  show information about specify .vhd file
  --help                       Show this message and exit.
```
