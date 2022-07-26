
nums=[1,2,3,1,2,3]


def containsNearbyDuplicate(nums:list,k:int) -> bool:
        for i in nums:
            idxs=[]
            for idx in range(len(nums)):
                if nums[idx]==i:
                    idxs.append(idx)
            for ind in idxs:
                for n in range(idxs.index(ind)+1,len(idxs)):
                    if abs(ind-idxs[n])<=k:
                        return True
        else:
            return False




print(containsNearbyDuplicate(nums,2))

