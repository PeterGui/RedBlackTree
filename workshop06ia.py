'''
Created on Sep 23, 2015

@author: gkalmanovich
'''
import time
import numpy as np
import numpy.random as nprnd
import matplotlib.pyplot as pplot
from binarySearchTreeWorkshop import Node

n=5
array_of_n = []
insert_time = []
lookup_time = []
delete_time = []
insertRBT_time = []
lookupRBT_time = []
deleteRBT_time = []
for i in range(50):
    arr      = nprnd.randint(0,1000000,n)
    arr_diff = nprnd.randint(0,1000000,n)
    arr_copy = np.copy(arr)
    arr_copy = np.random.permutation(arr_copy)

    array_of_n.append(n)

    # Insert
    start = time.clock()
    root    = Node(arr[0])
    for j in range(1,n):
        root.insert(arr[j])
    insert_time.append(time.clock()-start)
    start = time.clock()
    '''TODO: Change the node below to an NodeRBT'''
    rootRBT = Node(arr[0]) 
    for j in range(1,n):
        rootRBT.insert(arr[j])
    insertRBT_time.append(time.clock()-start)

    # Look up
    start = time.clock()
    for j in range(0,n):
        """??? TODO: Uncomment after look up works ???"""
        #prnt,node = root.lookup(arr_diff[j])
    lookup_time.append(time.clock()-start)
    start = time.clock()
    for j in range(0,n):
        """??? TODO: Uncomment after look up works ???"""
        #prnt,node = rootRBT.lookup(arr_diff[j])
    lookupRBT_time.append(time.clock()-start)
    
    # Delete
    start = time.clock()
    for j in range(0,n):
        prnt, node = root.lookup(arr[j])
        """??? TODO: Uncomment after look up works ???"""
        #root = root.deleteNode(node, prnt, root)
    delete_time.append(time.clock()-start)
    # Delete
    start = time.clock()
    for j in range(0,n):
        prnt, node = rootRBT.lookup(arr[j])
        """??? TODO: Uncomment after look up works ???"""
        #root = rootRBT.deleteNode(node, prnt, rootRBT)
    deleteRBT_time.append(time.clock()-start)
   

    n = int(n*1.2)
    
# Do plots for selection sort here
    
pplot.plot(array_of_n,np.array(insert_time)/(np.array(array_of_n)*np.log(np.array(array_of_n))),array_of_n,np.array(insertRBT_time)/(np.array(array_of_n)*np.log(np.array(array_of_n))))
pplot.xscale('log')
pplot.show()

"""??? TODO: Two more plots (look up and delete) ???"""

'''TODO, now redo the above with 
    arr      = range(n)
    you will likely need to reduce the number of iterations the outside loop does, e.g., 50->15)'''
    



