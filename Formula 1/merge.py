import pandas as pd
import numpy as np
import fileinput

def merge_driver(year, race):

    for i in range(race):
        locals()['df' + str(race - i)] = pd.read_csv('csvs/standings/standings_' + str(year) + '_' + str(race - i) + '.csv', usecols=[0, 1])
        if(i > 0):
            locals()['df' + str(race)] = pd.merge(eval('df' + str(race - i)), eval('df' + str(race)), on = 'name', how = 'outer')

    eval('df' + str(race)).set_index('name', inplace = True)
    eval('df' + str(race)).to_csv('csvs/position/' + str(year)+'_position.csv')

# def merge_constructor(year, race):
#
#     for i in range(race):
#         locals()['df' + str(race - i)] = pd.read_csv('csvs/standings_' + str(year) + '_' + str(race - i) + '.csv', usecols=[0, 1])
#         if(i > 0):
#             locals()['df' + str(race)] = eval('df' + str(race)).merge(eval('df' + str(race - i)), on = 'name')

def pos_int(year):
    file_in = 'csvs/position/' + str(year) + '_position.csv'
    file_out = 'csvs/' + str(year) + '_points_old.csv'
    with fileinput.FileInput(file_in, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('.0,', ',').replace('.0\n', '\n'), end='')

def separator(year):
    file_in = 'csvs/position/' + str(year) + '_position.csv'
    with fileinput.FileInput(file_in, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(',1,', ',1.0,').replace(',2,', ',2.0,').replace(',3,', ',3.0,').replace(',4,', ',4.0,')
                  .replace(',8,', ',8.0,').replace(',7,', ',7.0,').replace(',6,', ',6.0,').replace(',5,', ',5.0,')
                  .replace(',9,', ',9.0,').replace(',1\n', ',1.0\n').replace(',2\n', ',2.0\n').replace(',3\n', ',3.0\n')
                  .replace(',7\n', ',7.0\n').replace(',6\n', ',6.0\n').replace(',5\n', ',5.0\n').replace(',4\n', ',4.0\n')
                  .replace(',8\n', ',8.0\n').replace(',9\n', ',9.0\n')
                  , end='')
#
# def separator_double(year):
#     file_in = 'csvs/position/' + str(year) + '_position.csv'
#     with fileinput.FileInput(file_in, inplace=True, backup='.bak') as file:
#         for line in file:
#             print(line.replace(',10', ',10').replace('_11', '_11*')
#                   .replace('_12', '_12*').replace('_13', '_13*').replace('_14', '_14*').replace('_15', '_15*')
#                   .replace('_16', '_16*').replace('_17', '_17*').replace('_18', '_18*').replace('_19', '_19*')
#                   , end='')


def pos_point(year):
    file_in = 'csvs/position/' + str(year) + '_position.csv'
    file_old = 'csvs/points/' + str(year) + '_points_old.csv'
    file_new = 'csvs/points/' + str(year) + '_points_new.csv'
    with open(file_in, "rt") as fin:
        with open(file_old, "wt") as fout:
            for line in fin:
                fout.write(line.replace(',1.0', ',*10').replace(',2.0', ',*8').replace(',3.0', ',*6').replace(',4.0', ',*5').replace(
                    ',5.0', ',*4').replace(',6.0', ',*3').replace(',7.0', ',*2').replace(',8.0', ',*1').replace(',9.0', ',0').replace(
                    ',10', ',0').replace(',11', ',0').replace(',12', ',0').replace(',13', ',0').replace(
                    ',14', ',0').replace(',15', ',0').replace(',16', ',0').replace(',17', ',0').replace(
                    ',18', ',0').replace(',19', ',0').replace(',20', ',0').replace(',21', ',0').replace(
                    ',22', ',0').replace(',23', ',0').replace('position', 'point').replace(',,', ',0,')
                           .replace('0,,', '0,0,'))
            fout.close()
        fin.close()
    with fileinput.FileInput(file_old, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(',*', ','), end='')

    with open(file_in, 'rt') as fin:
        with open(file_new, "wt") as fout1:
            for line in fin:
                fout1.write(line.replace(',1.0', ',*25').replace(',2.0', ',*18').replace(',3.0', ',*15').replace(
                    ',4.0', ',*12').replace(',5.0', ',*10').replace(',6.0', ',*8').replace(',7.0', ',*6').replace(
                    ',8.0', ',*4').replace(',9.0', ',*2').replace(',10', ',*1').replace(',11', ',0').replace(
                    ',12', ',0').replace(',13', ',0').replace(',14', ',0').replace(',15', ',0').replace(
                    ',16', ',0').replace(',17', ',0').replace(',18', ',0').replace(',19', ',0').replace(
                    ',20', ',0').replace(',21', ',0').replace(',22', ',0').replace(',23', ',0')
                           .replace('position', 'point').replace(',,', ',0,').replace('0,,', '0,0,'))
            fout1.close()
    fin.close()
    with fileinput.FileInput(file_new, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(',*', ','), end='')