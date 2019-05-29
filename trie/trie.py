#code


class trie_node:
   
   def __init__(self):
      self.trie = [None]*26
      self.isLeaf =False
   
   
   def insert(self,string):

      for c in string:
         
         if self.trie[ord(c)-ord('a')] == None:
            self.trie[ord(c)-ord('a')] = trie_node()
         
         self = self.trie[ord(c)-ord('a')]
         
      self.isLeaf = True
      
   
   def search(self,string):
      
      for c in string:
         if self.trie[ord(c)-ord('a')] == None:
            return False
         
         self = self.trie[ord(c)-ord('a')]
      
      if(self.isLeaf == False):
         return False
      return True
   

t = trie_node()
t.insert('a')
t.insert("an")
t.insert("the")
print("Search result for 'the':",t.search("the"))
print("Search result for 'ther':",t.search("ther"))
print("Search result for 'a':",t.search("a"))
print("Search result for 'ann'",t.search("ann"))
