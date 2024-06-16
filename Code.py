class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = {}
        for x in range(len(names)):
            d[heights[x]] = names[x]
        height = sorted(heights,reverse = True)
        name = []
        for y in range(len(names)):
            name.append(d[height[y]])
        return name
        
            
