from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        prev_len = len(chars)

        if prev_len < 2:
            return prev_len

        insertion_index = 0
        char_repetition = 1

        current_char_index = 0
        is_last = False
        for index in range(prev_len):
            if is_last:
                not_equal = True
            else:
                not_equal = chars[current_char_index] != chars[index + 1]

            if not_equal:
                current_char_index = current_char_index if not is_last else index
                chars[insertion_index] = chars[current_char_index]
                insertion_index += 1

                if char_repetition > 1:
                    for repetition in str(char_repetition):
                        chars[insertion_index] = repetition
                        insertion_index += 1

                char_repetition = 1
                current_char_index = index + 1
            else:
                char_repetition += 1

            is_last = index == prev_len - 2

        for i in range(prev_len - insertion_index):
            chars.pop()
        return len(chars)