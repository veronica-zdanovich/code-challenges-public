class Solution:
    def solve_equation_part(self, equation_part: str):
        index = 0
        x_coefficient = 0
        sum_coefficient = 0

        while index < len(equation_part):
            char = equation_part[index]

            match char:
                case "-":
                    sign = -1
                    index += 1
                case "+":
                    sign = 1
                    index += 1
                case _:
                    sign = 1

            term = list()
            x_found = False
            while index < len(equation_part) and equation_part[index] not in ["-", "+"]:
                if equation_part[index] == "x":
                    x_found = True
                    index += 1
                    break
                term.append(equation_part[index])
                index += 1

            coefficient = int("".join(term)) if len(term) > 0 else 1
            if x_found:
                x_coefficient += sign * coefficient
            else:
                sum_coefficient += sign * coefficient

        return x_coefficient, sum_coefficient

    def solveEquation(self, equation: str) -> str:
        x_coefficient = 0
        sum_coefficient = 0
        side = 1

        sum_on_right = -1

        for part in equation.split("="):
            x_part, sum_part = self.solve_equation_part(part)

            x_coefficient += x_part * side
            sum_coefficient += sum_part * side * sum_on_right

            side *= -1

        if sum_coefficient == 0 and x_coefficient == 0:
            return "Infinite solutions"

        if x_coefficient == 0:
            return "No solution"

        return f"x={sum_coefficient // x_coefficient}"
