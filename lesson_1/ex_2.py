time = int(input('time in sec.: '))
print(f'{(time // 3600):02}:'
      f'{((time % 3600) // 60):02}:'
      f'{(time % 60):02}')
