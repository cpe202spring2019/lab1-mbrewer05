
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)\
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError
   if int_list == []:
      return None
   result = int_list[0]
   for x in int_list:
      if x > result:
         result = x
   return result

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError
   if len(int_list) == 1:
      return int_list
   temp_list = int_list[1:len(int_list)]
   new_list = reverse_rec(temp_list)
   new_list.append(int_list[0])
   return new_list

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list == None:
      raise ValueError
   if high < low:
      return None
   mid = (high + low) // 2
   if int_list[mid] == target:
      return mid
   elif int_list[mid] < target:
      return bin_search(target, mid + 1, high, int_list)
   elif int_list[mid] > target:
      return bin_search(target, low, mid - 1, int_list)