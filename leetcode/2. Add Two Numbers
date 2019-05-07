# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val = 0
        val2 = 0
        
        isThereCarry = False
        resultPrev = None
        resultHead = None
        while (l1 != None or l2 != None) or isThereCarry == True:
            result = None
            if(l1 != None):
                val = l1.val
                l1 = l1.next
                #print(val)
            else:
                val = 0
            if l2 != None :
                val2 = l2.val
                l2 = l2.next
            else : 
                val2 = 0
            
            if isThereCarry:
                sum = val + val2 + 1
            else :
                sum = val + val2
            
            if(resultPrev == None) :
                if (sum >= 10) :
                    resultPrev = ListNode(sum % 10)
                    isThereCarry = True
                else : 
                    resultPrev = ListNode(sum)
                    isThereCarry = False
                resultHead = resultPrev
                    
            else : 
                result = ListNode(0)
                if(sum >= 10):
                    isThereCarry = True
                    result.val = sum % 10
                else : 
                    isThereCarry = False
                    result.val = sum
                
                resultPrev.next = result
                resultPrev = result
        return resultHead
            
        
