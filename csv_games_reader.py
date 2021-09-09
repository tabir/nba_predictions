import csv
import os
import re
import datetime as dt
from datetime import timedelta
from pytz import timezone
csv_dir='/input/'
outpot_dir='/output/'
#files=['October_games.csv', 'November_games.csv', 'December_games.csv', 'January_games.csv', 'February_games.csv', 'March_games.csv', 'April_games.csv']
files=['October_games.csv']
append_to_file={filename:[] for filename in files}
next_file={files[i]:files[i+1] for i in range(len(files)-1)}
prev_sheet='template'
for filename in files:
  match = re.match(r"(.*)\.csv", filename)
  if match:
    print(filename)
    current_sheet=match.groups()[0]
    with open(csv_dir+filename, 'r') as csvfile:
      reader = csv.reader(csvfile, delimiter=',', quotechar='\"')
      first=True
      first_data = True
      for row in reader:
        if first:
          first=False
        else:
          if row[1]=="":
            row[1]="4:30p"
          date_time_obj = dt.datetime.strptime(row[0] + " " + row[1] + "m", '%a %b %d %Y %I:%M%p')
          eastern = timezone('US/Eastern')
          date_time_obj = eastern.localize(date_time_obj)
          date_time_obj = date_time_obj.astimezone(timezone('Israel'))
          row.remove(row[5])
          game_night_obj = date_time_obj - timedelta(hours=12)
          curr_row = [game_night_obj.strftime('%a %b %d')] + [date_time_obj.strftime('%a %b %d')]+[date_time_obj.strftime('%H:%M')]+[row[3]] + [row[2]]
          if first_data:
            month = game_night_obj.strftime('%b')
            first_data = False
          if month != game_night_obj.strftime('%b'):
            append_to_file[next_file[filename]] = append_to_file[next_file[filename]] + [curr_row]
          else:
            append_to_file[filename] = append_to_file[filename] + [curr_row]
      with open(outpot_dir+filename, 'w') as outcsvfile:
        writer = csv.writer(outcsvfile, delimiter=' ',
                            quotechar='\"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['#Games',str(len(append_to_file[filename])),'Prev',prev_sheet])
        writer.writerow([' ',' ',' ',' ',' ',' ','Predictions'])
        writer.writerow(['Game_night','Date','Time','Home','Visitor','Elad','Oz','Ofer','Tal','Results'])
        for curr_row in append_to_file[filename]:
          writer.writerow(curr_row)
      prev_sheet = current_sheet 
