from datetime import date, time, datetime, timedelta

def work(dd):
  print("hello world."+str(dd))



def runTask(func, day, hour=0, min=0, second=0):
  # Init time
  now = datetime.now()
  strnow = now.strftime('%Y-%m-%d %H:%M:%S')
  print("now:", strnow)
  # First next run time
  period = timedelta(days=0, hours=hour, minutes=min, seconds=second)
  next_time = now + period
  strnext_time = next_time.strftime('%Y-%m-%d %H:%M:%S')
  print("next run:", strnext_time)
  flag = setFlag(day)
  while flag:
      # Get system current time
      iter_now = datetime.now()
      iter_now_time = iter_now.strftime('%Y-%m-%d %H:%M:%S')
      if str(iter_now_time) == str(strnext_time):
          # Get every start work time
          print("start work: %s" % iter_now_time)
          # Call task func
          func()
          print("task done.")
          # Get next iteration time
          iter_time = iter_now + period
          strnext_time = iter_time.strftime('%Y-%m-%d %H:%M:%S')
          print("next_iter: %s" % strnext_time)
          # Continue next iteration
          continue

def setFlag(flag):
    if flag == True:
        return True
    else :
        return False


# runTask(work, min=0.5)
runTask(work, day=False, hour=0, min=0, second=1)
for i in range(0, 10):
    if i ==5:
        day = False
    else:
        day = True

    runTask(work(i), day=day, hour=0, min=0, second=1)

