#This program is designed to provide an example for linked lists while demonstrating node manipulation

#Creates a new node 
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  #Retrieves the value of the node 
  def get_value(self):
    return self.value
  
  #Retrieves the value of the next node
  def get_next_node(self):
    return self.next_node
  
  #Sets the value of the next node
  def set_next_node(self, next_node):
    self.next_node = next_node

#Creates a Linked List
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  #Retrieves the value of the head node in the following node string
  def get_head_node(self):
    return self.head_node
  
  #Sets a new head node at the beginning of the node string
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  #Creates a list of nodes, each node listed within a new line 
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
  #Removes a node from the node list and changes the links to prevent orphaned nodes
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node

