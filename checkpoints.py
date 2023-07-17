class Solution:    
    def longestdistance(self, checkpoints):
            # Sort checkpoints from least to greatest
            #type num: list of int
            #return type: int
            i = 0
            #TODO: Write code below to returnn an int with the solution to the prompt.
            while (i < (len(checkpoints)-2)):
                checkpoint = checkpoints[i]
                if (checkpoint > checkpoints[i + 1]):
                     checkpoints[i] = checkpoints[i+1]
                     checkpoints[i+1] = checkpoint
                     if i > 0:
                         i = i - 1
                else:
                    i = i+1
            greatest = 0    
            for i in range(len(checkpoints)-1):
                if (checkpoints[i+1]-checkpoints[i]) > greatest:
                     greatest = checkpoints[i]
            print(greatest)
                     

            
            pass

def main():
    array = input().split(" ")
    for x in range (0, len(array)):
        array[x] = int(array[x])

    tc1 = Solution()
    ans = tc1.longestdistance(array)
    print(ans)

if __name__ and "__main__":
    main()
