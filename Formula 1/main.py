import data_grabber
import merge
import glob

# for i in range(2000, 2017):
#     for j in range(1, 22):
#         temp = data_grabber.standings_xml(i, j)
#         if(temp):
#             continue
#             data_grabber.convert(i, j)
#         else:
#             break

# races = []
# for i in range(2000, 2017):
#     total = 0
#     for name in glob.glob('csvs/standings/standings_' + str(i) + '_*.csv'):
#         total = total + 1
#     races.append(total)
#
# for i in range(2000, 2017):
#     race = races[i - 2000]
#     merge.merge_driver(i, race)
#     # merge.merge_constructor(i, race)
#
# for i in range(2000, 2017):
#     merge.pos_int(i)

for i in range(2000, 2017):
    merge.separator(i)
    merge.separator(i)
    merge.pos_point(i)
    merge.pos_point(i)
    merge.pos_int(i)