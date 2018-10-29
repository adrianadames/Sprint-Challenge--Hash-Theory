# Given a package with a weight limit limit and a list weights of item weights, 
# implement a function get_indices_of_item_weights that finds two items whose 
# sum of weights equals the weight limit limit. Your function should return a 
# tuple (i, j) of the indices of the item weights, ordered such that i > j. If 
# such a pair doesn’t exist, return an empty tuple.

# Your solution should run in linear time.

#given the list weights of item weights, return the index of the two weights (as a tuple) that add up to limit
def get_indices_of_item_weights(weights, limit):
  #step 1: instantiate hash table
  weights_dict = {}
  #step 2: populate weights_dict hash table with the weights in weights as keys and the index of the weight in the array as the corresponding value.
  for i in range(0,len(weights)): #range doesn't include len(weights) in the range
    weight = weights[i]
    # print(weight)
    # print(limit-weight)
    if limit-weight in weights_dict:
      # print("limit-weight is in weights")
      if i >= weights_dict[limit-weight]:
        # print(i, weights_dict[limit-weight])
        return (i, weights_dict[limit-weight])
      else:
        # print(weights_dict[limit-weight], i)
        return (weights_dict[limit-weight], i)
    else: 
      weights_dict[weight] = i
      # print(weights_dict[weight])
  return () 


weights_test1 = [4, 6, 10, 15, 16]
weights_test2 = [4, 4]
limit_test1 = 21
limit_test2 = 8
print(get_indices_of_item_weights(weights_test2, limit_test2))


if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  pass 