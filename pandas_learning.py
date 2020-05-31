import itertools
import pandas as pd
import time
#
# print(type(dup['%sys']))
# # print(df1.head(5))
#
#
#
# # df1 = pd.read_csv('combined_data1.csv')
# # df2 = pd.read_csv('vmstat.csv')
# # print(len(df2))
# # print(len(df1))
# dup = data_merge.drop_duplicates(subset=['Time', 'CPU', 'Inactive', 'Active', 'Used'], keep='last')
# print(len(dup))
# # print(dup.head(20))
# #
# dup.to_csv('combined_data1.csv', index= False)

# df1 = pd.read_csv('combined_data1.csv')
# df2 = pd.read_csv('pidstat.csv')
# df_merge = pd.merge(df1, df2, on='Time', how='outer')
# print(df_merge.head(10))
# print(len(df_merge))
# df_merge.to_csv('dup2.csv', index=False)
# dup = df_merge.drop_duplicates(subset=['Time', 'CPU_x', 'Command'], keep='last')
# print(len(dup))
# print(dup.head(25))
# dup.to_csv('dup3.csv', index=False)
#
# print(len(df4))
# print(df4.head(15))
# df4.to_csv('dup4.csv', index=False)
#
# print(len(df6))
# print(df6.head(15))
#
#
# df = pd.read_csv('combined_data2.csv')
# print(len(df))
# print(df.loc[df['Time']=='4:02:55 AM'])






# print(data_outer.head(20))
# data3 = pd.read_csv('pidstat.csv', delimiter=',')
# data_outer1 = pd.merge(data_outer, data3, on='Time', how='outer')
# print(data_outer1.head(20))
# data4 = pd.read_csv('vmstat.csv', delimiter=',')
# data_outer2 = pd.merge(data_outer1, data4, on='Time', how='outer')

# print(data1.tail(10))
# print(data1.columns)
# print(data1[['Time', 'Flow_count']][0:20])
# print(data1['Time'].iloc[0:10])
# data2 = pd.read_csv('mpstat.csv')
# print(data2)
# print(data2.tail(10))
# print(data1.count(1))
# if data1[data1.Time].head(1) == data2[data2.Time].head(1):
#     print('Matched')

# print( data1.iloc[1, 0])
# for r1, r2 in itertools.zip_longest(data1.iterrows(), data2.iterrows()):
#     if data1.iloc[, 0] == data2.iloc[r2, 0]:
#         print('Matched')
#     else:
#         print('Not matched')
# print(len(data1))
# for index1 in range(len(data1)):
#     print(data1.iloc[index1, 0])
    # print(data1.iloc[index1 - 1, 0])

# print(data1.loc[data1['Flow_count']== 65740])

# data1 = data1.drop(columns=['Delta(flows)'])
# print(data1.head(5))
# print(data1.iloc[25:35])

# data1['Delta(flows)'] = data1.iloc[:, 1:1].add(axis=0)
# print(type(data1.iloc[2,0]))
# date1 = data1.iloc[2,0]
# print(date1)
# time_str1 = data1.iloc[2, 0]
# print(time_str1)
# # time_str2 = data2.iloc[2, 0]
# time1 = time.strptime(time_str1, "%H:%M:%S %p")
# # time1.strptime("%I:%M:%S %p")
# print(type(time1))
# print(time1)
# r1 = 2
# r2 = 2
# insert_data = []
# max_r1 = len(data1)
# max_r2 = len(data2)
# print(max_r1, max_r2)
# while r1 < 10 and r2 < 10:
#     insert_data.clear()
#     new_r1 = r1
#     new_r2 = r2
#     time_str1 = data1.iloc[r1, 0]
#     time_str2 = data2.iloc[r2, 0]
#     print(time_str1)
#     print(time_str2)
#     time1 = time.strptime(time_str1, "%I:%M:%S %p")
#     time2 = time.strptime(time_str2, "%I:%M:%S %p")
#     if time1 == time2:
#         print('Match')
#         data1['CPU'] = data2['CPU']
#         # r1 += 1
#         # r2 += 1
#
#     elif time1 < time2:
#         print('Less')
#         new_r1 += 1
#         print(new_r1)
#         time_str1 = data1.iloc[new_r1, 0]
#         print(time_str1)
#         time1 = time.strptime(time_str1, "%I:%M:%S %p")
#         while time1 < time2:
#             new_r1 += 1
#             print(new_r1)
#             time_str1 = data1.iloc[new_r1, 0]
#             # print(time_str1)
#             time1 = time.strptime(time_str1, "%I:%M:%S %p")
#         else:
#             if time1 == time2:
#                 # insert_data.insert(0, data2.iloc[r2,0])
#                 # insert_data.insert(1, data2.iloc[r2,1])
#                 # line = data1.DataFrame({'Time': insert_data[0], 'CPU': insert_data[1]}, index=[new_r1])
#                 # data1.append(line, ignore_index=False)
#
#                 data1['Time_new'] = data2['Date']
#                 data1['CPU'] = data2['CPU']
#
#
#                 # r2 += 1
#
#     elif time1 > time2:
#         print('Great')
#         new_r1 -= 1
#         print(new_r1)
#         time_str1 = data1.iloc[new_r1, 0]
#         print(time_str1)
#         time1 = time.strptime(time_str1, "%I:%M:%S %p")
#         while time1 > time2:
#             new_r1 -= 1
#             print(new_r1)
#             time_str1 = data1.iloc[new_r1, 0]
#             time1 = time.strptime(time_str1, "%I:%M:%S %p")
#         else:
#             if time1 == time2:
#                 # insert_data.insert(0, data2.iloc[r2, 0])
#                 # insert_data.insert(1, data2.iloc[r2, 1])
#                 # line = data1.DataFrame({'Time': insert_data[0], 'CPU': insert_data[1]}, index=[new_r1])
#                 # data1.append(line, ignore_index=False)
#                 data1['Time_new'] = data2['Date']
#                 data1['CPU'] = data2['CPU']
#                  # r2 += 1
#     r1 += 1
#     r2 += 1

# print(data1.sort_values('Time', ascending=False)
# print(data1.tail(15))
# data_outer.to_csv('handoff_mpstat.csv')
# df = pd.read_csv('flow_handoff_mpstat_pidstat_vmstat.csv')
# print(len(df))
df1 = pd.read_csv('combined_data2.csv')
df2 = df1.loc[(pd.to_numeric(df1['Drops'], errors='coerce')) == 737790 ]
# df2 = df1.loc[df1['%idle'] == 0]
print(df2.head(20))
# print(type(df['%idle']))
# df2 = df1[['%usr_x', '%sys', '%idle', 'UID', 'PID', '%usr_y', '%system', '%guest', '%Cpu', 'CPU_y', 'Command', 'Inactive', 'Active', 'Used']]
# df3 = df2.drop_duplicates(keep='last', inplace=False)
# print(df3)
# df3.to_csv('filtered.csv')
# print(len(df))
# df1 = df.drop_duplicates(keep='last')
# print(len(df1))
# df1.to_csv('dupoff_handoff_mpstat.csv')
# print(len(df1))
# data_outer1.to_csv('handoff_mpstat_pidstat.csv')
# data_outer2.to_csv('flow_handoff_mpstat_pidstat_vmstat.csv')


# if data1.loc['Time'] == data2.loc['Time']:
#     data1['CPU'] = data2['CPU']
# else:
# data1['CPU'] = data2['CPU']
# data1['Time']
# print(data1.head(10))