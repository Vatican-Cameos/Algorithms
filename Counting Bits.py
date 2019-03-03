import math;
class Solution:
    # DP : Recurrence relation . If odd : opt[i] = opt[i-1] + 1
    # Dp if even and in power of 2 series opt[i] = 1 else opt[i] = opt[j] +  opt[i-j] 
    def isIn2PowerSeries(self, value) -> bool:
            value = math.log(value,2) 
            if(value.is_integer()):
                return True
            else:
                return False
            
    def countBits(self, num: int) -> List[int]:
        opt = [None] * (num + 1)
        
        opt[0] = 0
        j = 0
        
        for i in range(1, num + 1):
            if(i % 2 == 0):     
                if(Solution.isIn2PowerSeries(self,i)):
                    opt[i] = 1
                    j = i
                else:
                    opt[i] = opt[j] + opt[i-j]
            else:
                opt[i] = opt[i-1] + 1
        return opt
    
    
                
                
            
        
