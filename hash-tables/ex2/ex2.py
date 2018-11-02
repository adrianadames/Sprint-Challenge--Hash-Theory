def reconstruct_trip(tickets):
  tickets_dict = {}

  route = [''] * (len(tickets)-1)

  for ticket in tickets:
    tickets_dict[ticket[0]] = ticket[1] #starting location is key and destination is value
    if ticket[0] == None: #if ticket doesn't have a starting location, then its destination is the first layover airport
      route[0] = ticket[1]

  for i in range(1,(len(tickets)-1)):
    if route[i-1] in tickets_dict:
      route[i] = tickets_dict[route[i-1]]
    else:
      return []
  
  print(route)
  return route
  

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  pass


# short_set = [
#       (None, 'PDX'),
#       ('PDX', 'DCA'),
#       ('DCA', None)
#     ]

# long_set = [
#       ('PIT', 'ORD'),
#       ('XNA', 'CID'),
#       ('SFO', 'BHM'),
#       ('FLG', 'XNA'),
#       (None, 'LAX'), 
#       ('LAX', 'SFO'),
#       ('CID', 'SLC'),
#       ('ORD', None),
#       ('SLC', 'PIT'),
#       ('BHM', 'FLG'),
#     ]

# reconstruct_trip(long_set)