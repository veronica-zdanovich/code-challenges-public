class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        max_col = len(s) + 1
        max_row = len(p) + 1
        matrix = [False for _ in range(max_row * max_col)]
        matrix[0] = True

        for row in range(1, max_row):
            if p[row - 1] != "*":
                break

            for col in range(0, max_col):
                matrix[row * max_col + col] = True

        for row in range(1, max_row):
            is_asterisk = False
            match p[row - 1]:
                case "*":
                    found_match = True
                    is_spec_char = True
                    is_asterisk = True
                case "?":
                    is_spec_char = True
                    found_match = True
                case _:
                    is_spec_char = False
                    found_match = False

            current_row = row * max_col
            prev_row = (row - 1) * max_col

            for col in range(1, max_col):
                prev_i = matrix[prev_row + col]
                prev_j = matrix[current_row + col - 1]
                prev_diag = matrix[prev_row + col - 1]

                if is_asterisk:
                    matrix[current_row + col] = prev_i or prev_j or prev_diag
                    continue

                if not is_spec_char:
                    found_match = s[col - 1] == p[row - 1]

                matrix[current_row + col] = prev_diag and found_match

            if sum(matrix[current_row: current_row + max_col]) == 0:
                return False

        return matrix[max_row * max_col - 1]
