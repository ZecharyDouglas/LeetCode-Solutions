class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        #find the boxes types with the highest number of units , and take up to truckSize number of them
        # sort the 2d array by the units from largest to smallest
        # ans variable
        # iterate through taking either numberOfBoxes[i] or remaining truckSize of them (min of either)
        # while truckSize > 0
            #add number of units to answer variable
            #decrease truckSize by numberOfUnitsPerBoxi 
        sortedBoxTypes = sorted( boxTypes ,key= lambda x : x[1] , reverse=True)
        ans=0
        for numBoxes , unitsPerBox in sortedBoxTypes:
            maxPossibleBoxes = min(truckSize , numBoxes)
            maxPossibleUnits= maxPossibleBoxes * unitsPerBox
            ans+=maxPossibleUnits
            truckSize -= maxPossibleBoxes
            if truckSize == 0:
                break
        return ans
            