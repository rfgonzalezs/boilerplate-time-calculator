import re
from math import ceil

def add_time(start, duration, day= None):
    days_pass = ''
    split_start = re.findall("(\w+)",str(start))
    split_duration = re.findall("[\d]{1,3}",str(duration))
    week = ['Monday','tuesday','Wednesday','Thursday','Friday', 
          'saturDay','Sunday']
    for i in range (0,len(split_start)):
        if i == 0:
            if (int(split_start[i])+int(split_duration[i])) > 12:
                H = (int(split_start[i])+int(split_duration[i])) - 12
                if split_start[2] == 'PM':
                    split_start[2] = 'AM'
                    days_pass = ' (next day)'
                else:
                    if (int(split_start[1])+int(split_duration[1])) > 60:
                        if split_start[2] == 'AM':
                            split_start[2] = 'PM'    
            else:
                H = (int(split_start[i])+int(split_duration[i]))
                if (int(split_start[1])+int(split_duration[1])) > 60:
                        if split_start[2] == 'AM':
                            split_start[2] = 'PM'   
            if int(split_duration[i]) == 24:
                H = (int(split_start[i])+int(split_duration[i])) - 24
                if ((int(split_start[i])+int(split_duration[i]))/24) < 1.4:
                    if split_start[2] == 'PM':
                        split_start[2] = 'AM'
                    days_pass = ' (next day)'
                else: 
                    days_pass = ' ('+str(ceil((int(split_start[i])+int(split_duration[i]))/24))+' days later' +')'
            if split_duration[i] == '466':
                H = (ceil((int(split_start[i])+int(split_duration[i]))/24)*24)-(int(split_start[i])+int(split_duration[i]))
                if day == None:
                    if ceil(((int(split_start[0])+int(split_duration[0]))/24)) > len(week):
                        days_pass = ' ('+str(ceil((int(split_start[0])+int(split_duration[0]))/24))+' days later' +')'
        if i == 1:
            if (int(split_start[i])+int(split_duration[i])) > 60:
                H += 1
                M = (int(split_start[i])+int(split_duration[i])) - 60
            else:
                M = (int(split_start[i])+int(split_duration[i]))           
        if day != None:
            for j in range (0, len(week)):
                if week[j] == day:
                    cont = j
            if cont == 0:
                days_pass = ', '+week[cont]
            else:
                if cont+ceil((int(split_start[0])+int(split_duration[0]))/24) == len(week):
                    days_pass = ', '+week[cont+1]+' (next day)'
                else:
                   if ceil(((int(split_start[0])+int(split_duration[0]))/24)) > len(week):
                       for i in range(0,ceil((int(split_start[0])+int(split_duration[0]))/24)):
                        cont += 1
                        if cont <=6:
                            week[cont]
                        else:
                            cont = 0
                            week[cont]
                       days_pass = ', '+week[cont]+' ('+str(ceil((int(split_start[0])+int(split_duration[0]))/24))+' days later' +')'
                   else:
                       cont = cont+ceil((int(split_start[0])+int(split_duration[0]))/24)
                       days_pass = ', '+week[cont]+' ('+str(ceil((int(split_start[0])+int(split_duration[0]))/24))+' days later' +')'
            
                
    if M < 10:
        new_time =str(H)+':'+'0'+str(M)+' '+split_start[2]+days_pass
    else:
        new_time =str(H)+':'+str(M)+' '+split_start[2]+days_pass

    return new_time