class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> anagramMap = new HashMap<>();

        for (String string : strs) {
            char[] chars = string.toCharArray();
            Arrays.sort(chars);
            String sortedString = new String(chars);

            if (anagramMap.containsKey(sortedString)) {
                anagramMap.get(sortedString).add(string);
            } else {
                anagramMap.put(sortedString, new ArrayList<>(Arrays.asList(string)));
            }
        }

        List<List<String>> result = new ArrayList<>();

        for (String key : anagramMap.keySet()) {
            result.add(anagramMap.get(key));
        }

        return result;
    }
}
