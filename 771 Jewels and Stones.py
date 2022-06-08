# You're given strings jewels representing the types of stones that are jewels, 
# and stones representing the stones you have. Each character in stones is a type of stone you have.
# You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        def split(word):
            return [char for char in word]
        
        jewelsType = split(jewels)
        stoneType = split(stones)
        numOfJewels = 0
        myStone = {}
        for stone in stoneType:
		# myStone.get(stone, 0) + 1 set value type as int the default value is 0
            myStone[stone] = myStone.get(stone, 0) + 1
        for stone in myStone:
            if stone in jewelsType:
				# myStone[stone] get value (number) of the jewels 
                numOfJewels += myStone[stone]
        return numOfJewels
