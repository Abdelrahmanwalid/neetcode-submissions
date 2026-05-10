class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
 
    hasDuplicate(nums) {
    let freqSet = new Set()
    for (let num of nums){
        freqSet.add(num)
    }
    if (freqSet.size === nums.length){
        return false
    }
    return true
    }

}
