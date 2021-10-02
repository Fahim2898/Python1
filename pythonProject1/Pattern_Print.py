'''
*
**
***
****
*****
'''
n=5
for i in range(n+1):
    print(i*'  *')

'''
    *
   **
  ***
 ****
*****
'''
n=5
for i in range(n+1):
    print((n-i)*' ' + i*'*')

'''
    *
   * *
  * * *
 * * * *
* * * * *
'''
n = 5
for i in range(n+1):
    print((n-i)*' ' +i*' *')