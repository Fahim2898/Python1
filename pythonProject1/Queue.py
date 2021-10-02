#Queue means FIFO(First-In First-Out)
#bank line
from collections import deque

bank = deque(['X', 'Y', 'Z', 'A'])
bank.append('W')
print(bank)
bank.popleft()
bank.popleft()
print(bank)

if not bank:
    print('No Person left')