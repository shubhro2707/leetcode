class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        return [item for item, freq in sorted_items[:k]]
