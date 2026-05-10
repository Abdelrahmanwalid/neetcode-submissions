class Solution:
    def countSeniors(self, details: List[str]) -> int:
        result = []
        for person in details:
            age = person[11] + person[12]
            if int(age) > 60:
                result.append(person)
        return len(result)