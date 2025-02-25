from datetime import datetime
wait_until = datetime.now().second + 2

while datetime.now().second != wait_until:
    1 + 1
    
print(f'We are at {wait_until} seconds!')
