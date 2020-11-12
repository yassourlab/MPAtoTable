MetaPhlAn3 filtretion by taxonomical level
==========================================
What is this?
-------------
This tool sorts and merges multiple MetaPhlAn3 output table files and creates a tab-seperated-value (.tsv) file with all results of the provided taxonomical level.
At the end of the process all given MetaPhlAn3 output files will be sorted into /unknown and /results folders, where /unknown folder will contain all 100% unknown (unmatched) results files.
**INPUT:** multiple MetaPhlAn3 output table files (Text file, usually ends with '.out')
**OUTPUT:** A single file, containing all organisms from provided files, fileterd to provided taxonomical level

How to use?
-----------
#### Commands
* Run tool (usage):
```
    ./metaphlan_runner <mpa_results.txt | folder/with/mpa/results> -f <taxonomical level> -o <out/dir/> [ADDITIONAL FLAGS][--help]
```
#### Examples
* Run tool on all mpa3 results in folder `my/mpa/folder` and filter only species (`-f s`). output results to `myResults/folder`
```
    ./metaphlan_runner my/mpa/folder -f s -o myResults/folder
```
* Run tool as in 1st example, but __copy__ (`-c`) mpa3 results to output destination. (default will move them there)
```
    ./metaphlan_runner my/mpa/folder -f s -o myResults/folder -c
```
* Run tool on `mpa1.txt` and `mpa2.txt` only and filter only by kingdom (`-f k`). output results to `myResults/folder`
```
    ./metaphlan_runner mpa1.txt mpa2.txt -f k -o myResults/folder
```
* View tool help
```
./metaphlan_runner  --help
```

Flags and running options
-------------------------
To see more options and flags please run:
`--help -h -H`  ---> View help and exit.
`--copy -c`     ---> Copy mpa3 results instead of moving them.
<br>
#### All available filters:
`k`=kingdom <br>
`p`=phylum<br>
`c`=class<br>
`o`=order<br>
`f`=family<br>
`g`=genus<br>
`s`=species
