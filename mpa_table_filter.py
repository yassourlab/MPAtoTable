#!/usr/bin/env python3

# ========================================================= #
# mpa_table_filter                                          #
# by Michael Sichenko - Yassour Lab - HUJI                  #
# version: 1.0                                              #
# ========================================================= #

import csv
import os
import sys
import argparse
import logging as log

TAXONOMIC_RANKS     = {'k': 'kingdom',
                       'p': 'phylum',
                       'c': 'class',
                       'o': 'order',
                       'f': 'family',
                       'g': 'genus',
                       's': 'species'
                       }
DESCRIPTION         = "Fitler the MPA pipeline table according to the set filter"
INPUT_HELP_INFILE   = "One tab-delimited values table to filter"
INPUT_HELP_TAX_LVL  = "Taxonomic rank classification filter:\n" + str(TAXONOMIC_RANKS)
INPUT_HELP_OUTPATH  = "Path of generated filtered results file"



def parse_input():
    """ parser of input """
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("in_file", metavar="mpa3_table.tsv", help=INPUT_HELP_INFILE)
    parser.add_argument("taxo_lvl", metavar="taxo_level",type=str, help=INPUT_HELP_TAX_LVL)
    parser.add_argument("out_file_path", metavar="path_to_out", default="mpa_filtered.txt", help=INPUT_HELP_OUTPATH)
    all_args = parser.parse_args()

    add_args_to_log(all_args)
    return all_args


def process_mpa(all_args):
    """
    filters the supplied in.tsv file according to supplied taxonomic level
    creates an out.tsv file and adds filtered data to it
    """
    tx_filter = str.lower(all_args.taxo_lvl)+'__'
    all_clades = set()
    with open(all_args.in_file) as in_file:
        tsv_reader = csv.reader(in_file, csv.excel_tab)
        # next(tsv_reader)    # skip first line

        # create output file and header
        header = next(tsv_reader)
        out_file_writer = create_out_file(all_args.out_file_path, header)

        # iterate to EOF and process data
        for line in tsv_reader:
            if tx_filter in line[0]:  # add line to file (no duplicates) if added - saved in the set
                all_clades.add(write_line_to_file(line, out_file_writer, tx_filter, all_clades))


def write_line_to_file(line, tsv_writer, tx_filter, all_clades):
    """
    writes line to tsv_writer obj if current line's clade hasn't appeared
    :return: (str) representing current line's clade
    """
    clades_split = (line[0].split('|')) # split at taxonomic level + '|X__'
    for item in clades_split:
        if tx_filter in item:
            line[0] = item[3:]   # the 3 is tho remove 'X__' of tax lvl
            break

    if line[0] not in all_clades:
        tsv_writer.writerow(line)

    return line[0]


def create_out_file(out_file_path, header):
    """
    init output file and add header row to it
    :return: writer obj of out.tsv file
    """
    # Create writer
    out_file = open(out_file_path, 'w+')
    tsv_writer = csv.writer(out_file, csv.excel_tab, lineterminator='\n')
    tsv_writer.writerow(header)
    return tsv_writer


def add_args_to_log(all_args):
    """
    adding all given system args to log
    """
    log.info('input_file='+all_args.in_file)
    log.info('taxonomic_filter_level='+all_args.taxo_lvl)
    log.info('output_file_path='+all_args.out_file_path)


def main():
    """
    main entry point for this module
    """
    # log prefs
    START_LOG_MSG   = '='*8 + 'START mpa_table_filter.py' + '='*8
    END_LOG_MSG     = '='*14 + 'END mpa_table_filter.py\n\n'
    log.basicConfig(filename='mpa_table_filter.log',
                    format='%(asctime)s - %(levelname)s::%(message)s',
                    level=log.INFO)

    # input processing
    log.info(START_LOG_MSG)
    all_args = parse_input();
    process_mpa(all_args)
    log.info(END_LOG_MSG)


if __name__ == "__main__":
    main()
