import time
import datetime

def countdown(dis):
    temp = dis
    days = int(temp / 86400)
    temp = temp % 86400
    hours = int(temp / 3600)
    temp = temp % 3600
    minutes = int(temp / 60)
    temp = temp % 60
    seconds = temp
    while(dis > 0):
        print(days,"days,",hours,"hours,",minutes,"minutes and ",seconds,"seconds.",end='\r')
        time.sleep(1)
        if(seconds == 0):
            seconds = 60
            minutes -= 1
            if(minutes == 0):
                minutes = 59
                hours -= 1
                if(hours == 0):
                    hours = 23
                    days -= 1
        dis -= 1
        seconds -= 1
    print("\a               !Countdown Ended!                    ")



def main():
    currentDate = datetime.datetime.now()
    givenDateYear = int(input("Enter the target Year:(current)") or currentDate.year)
    givenDateMonth = int(input("Enter the target Month:(current)") or currentDate.month)
    givenDateDay = int(input("Enter the target Date:(current)") or currentDate.day)
    givenDateHours = int(input("Enter the target Hour(24-hr format):(0)") or 0)
    givenDateMinute = int(input("Enter the target Minutes:(0)") or 0)
    givenDateSecond = int(input("Enter the target Second:(0)") or 0)
    givenDate = datetime.datetime(givenDateYear,givenDateMonth,givenDateDay,givenDateHours,givenDateMinute,givenDateSecond)
    duration  = givenDate - currentDate
    durationInSeconds = duration.seconds + (duration.days * 3600 * 24)
    if(durationInSeconds < 0):
        print("The Time has passed already")
        return 1
    countdown(durationInSeconds)

main()