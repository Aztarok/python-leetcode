class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = []
        dire = []
        for i, char in enumerate(senate):
            if char == "R":
                radiant.append(i)
            else:
                dire.append(i)
        maximum = len(senate)
        while True:
            print(radiant, dire)
            minimum = min(len(radiant), len(dire))
            if len(radiant) == 0 or len(dire) == 0:
                return "Radiant" if len(radiant) > 0 else "Dire"
            for i in range(minimum):
                if radiant[0] < dire[0]:
                    dire.pop(0)
                    radiant.pop(0)
                    radiant.append(maximum)
                    maximum += 1
                else:
                    radiant.pop(0)
                    dire.pop(0)
                    dire.append(maximum)
                    maximum += 1


def main():
    senate = "RDDRRRDDDRDR"
    solution = Solution()
    result = solution.predictPartyVictory(senate)
    print(result)


if __name__ == "__main__":
    main()
