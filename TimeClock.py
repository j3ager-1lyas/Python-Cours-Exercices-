import time

Time = time.localtime()
seconds=int(time.strftime("%S",Time))
minutes=int(time.strftime("%M",Time))
hours=int(time.strftime("%H",Time))

while(True):
    
    for hours in range(hours,24):
        
        for minutes in range(minutes,60):
            
            for seconds in range(seconds,60):
                print(f"{hours:0>2}:{minutes:0>2}:{seconds:0>2}")
                print(f"RealTime: {time.strftime('%H:%M:%S',time.localtime())}")
                time.sleep(1)
            seconds=0
        minutes=0
    hours=0