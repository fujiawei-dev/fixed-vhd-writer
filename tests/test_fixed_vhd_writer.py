'''
Date: 2022.02.05 17:34
Description: Omit
LastEditors: Rustle Karl
LastEditTime: 2022.02.05 17:34
'''
import gzip
import os
import shutil
import tempfile

from fixed_vhd_writer.vhd import FixedVHDWriter

cwd = os.path.abspath(os.path.dirname(__file__))


def test_fixed_vhd_writer():
    with tempfile.TemporaryDirectory() as tempdir:
        vhd_file = os.path.join(tempdir, 'mini.vhd')

        with gzip.open(os.path.join(cwd, 'data/mini.vhd.gz'), 'rb') as f_in:
            with open(vhd_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

        vhd = FixedVHDWriter(vhd_file)

        print('\n' + vhd.geometry)

        vhd.write_from_binary_file(os.path.join(cwd, 'data/mbr.bin'))
