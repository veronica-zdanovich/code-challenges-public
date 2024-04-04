from typing import List


class Solution:
    def combine(self, opened_parentheses: int, closed_parentheses: int, parentheses: str, result: List[str]):
        if opened_parentheses == 0 and closed_parentheses == 0:
            result.append(parentheses)
            return parentheses

        with_parenthesis = ""
        if opened_parentheses > 0:
            with_parenthesis = self.combine(opened_parentheses - 1, closed_parentheses, parentheses + "(", result)
        without_parenthesis = ""
        if closed_parentheses > 0 and opened_parentheses < closed_parentheses:
            without_parenthesis = self.combine(opened_parentheses, closed_parentheses - 1, parentheses + ")", result)

        return with_parenthesis + without_parenthesis

    def generateParenthesis(self, n: int) -> List[str]:
        valid_parentheses = list()
        self.combine(n, n, "", valid_parentheses)
        return valid_parentheses
