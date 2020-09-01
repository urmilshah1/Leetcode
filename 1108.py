class Solution:
    def defangIPaddr(self, address: str) -> str:
        newone = []
        for i in address:
            if(i=='.'):
                newone = address.replace('.','[.]')
        return newone
            
            
            
            # Initialized a new list using the replace function. I simply replaced the dot '.' with '[.]' and added it to the new list called newone.