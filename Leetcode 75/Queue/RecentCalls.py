class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0] < t - 3000:
            self.requests.pop(0)
        return len(self.requests)


def main() -> None:
    recentCounter = RecentCounter()
    print(recentCounter.ping(0))
    print(recentCounter.ping(1))
    print(recentCounter.ping(100))
    print(recentCounter.ping(3001))
    print(recentCounter.ping(3002))
    print(recentCounter.ping(4002))


if __name__ == "__main__":
    main()
