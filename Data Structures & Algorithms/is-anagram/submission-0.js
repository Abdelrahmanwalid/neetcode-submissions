class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
  let map = new Map()

  for (let char of s){
    map.set(char, (map.get(char)|| 0) + 1)
  }

  for (let char of t){
    if (!map.has(char)) return false; // Extra char in t
    map.set(char, map.get(char) - 1)
     if(map.get(char) === 0){
        map.delete(char)
    }

  }
  if (map.size === 0){
    return true
  }     
  return false
}}
