# Largest Time for Given Digits
#Given an array of 4 digits, return the largest 24 hour time that can be made.

#The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

#Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

 

#Example 1:

#Input: [1,2,3,4]
#Output: "23:41"
#Example 2:

#Input: [5,5,5,5]
#Output: ""
 

#Note:

#A.length == 4
#0 <= A[i] <= 9


class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        A.sort(reverse=True)
        digitOne = None
        digitTwo = None
        digitThree = None
        digitFour = None
        answer = ""
        digitIndex = 1;
        while(digitIndex <= 4):
            if(digitIndex == 1):
                for digit in A:
                    if(digit <= 2):
                        if(digit == 2):
                            nNum = 0;
                            for digit in A:
                                if(digit < 6):
                                    nNum += 1;
                            
                            if(nNum >= 3):
                                digitOne = 2;
                                break;  
                        else:
                            digitOne = digit;      
                            break;
                
                if(digitOne == None):
                    return ""
                else:
                    answer += str(digitOne) 
                    A.remove(digitOne)

            elif(digitIndex == 2):
                if(digitOne == 2):
                    for digit in A:
                        if(digit <= 3):
                            digitTwo = digit
                            break; 
                elif(digitOne <= 1):
                    digitTwo = A[0]

                if(digitTwo == None):
                    return ""
                else:
                    answer += str(digitTwo) + ":"
                    A.remove(digitTwo)

            elif(digitIndex == 3):
                for digit in A:
                    if(digit < 6):
                        digitThree = digit
                        break
                if(digitThree == None):
                    return ""
                else:
                    answer += str(digitThree)
                    A.remove(digitThree)
            else:
                digitFour = A[0]
                answer += str(digitFour)

            digitIndex += 1
        return answer
