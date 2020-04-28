#!/usr/bin/env python3 

import os
import sys
import errno

from mutate import Mutate  


def main():
    
    if len(sys.argv) != 3:
        print('Incorrect format')
        sys.exit(1)

    _, binary, fuzzer_dir = sys.argv

    #Find out where the directories are

    with open(os.path.join(fuzzer_dir, 'fuzz_bitmap'), 'rb') as bitmap_file:
        fuzzer_bitmap = bitmap_file.read()
    source_dir = os.path.join(fuzzer_dir, 'queue')
    dest_dir = os.path.join(fuzzer_dir, '..', 'mutate', 'queue')

    try:
        os.makedirs(dest_dir)
    except os.error as e:
        if e.errno != errno.EEXIST:
            raise

    seen = set()
    count = len(os.listdir(dest_dir))
    #print(source_dir, dest_dir, seen, count)
    

if __name__ == '__main__':
    main()
