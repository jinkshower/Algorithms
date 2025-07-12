class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # pairs = []

        # for spell in spells:
        #     count = 0
        #     for potion in potions:
        #         cur = spell * potion

        #         if cur >= success:
        #             count += 1
        #     pairs.append(count)
        
        # return pairs
        potions.sort()
        pairs = []

        def binarySearch(spell, potions):
            start = 0
            end = len(potions) - 1
            index = -1

            while start <= end:
                mid = (start + end) // 2
                cur = spell * potions[mid]
                
                if cur >= success: # True. memorize and search left
                    index = mid
                    end = mid - 1
                else: # False, search right
                    start = mid + 1
            return index

        for spell in spells:
            index = binarySearch(spell, potions)
            if index == -1:
                pairs.append(0)
            else:
                pairs.append(len(potions) - index)
        
        return pairs