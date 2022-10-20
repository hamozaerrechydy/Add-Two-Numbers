def reverse(l): 
  N = [] 
  N.append(l[2]) 
  N.append(l[1]) 
  N.append(l[0]) 
  return N

def list_to_int(l):
  s = [str(integer) for integer in reverse(l)]
  a_string = "".join(s)
  return int(a_string)

def addTwoNumbers(x, y): 
  s = list_to_int(x) + list_to_int(y) 
  a = [int(x) for x in str(s)]
  r = [ a[2], a[1], a[0]]
  
  return list(r)

print(addTwoNumbers([2,4,3], [5,6,4]))
