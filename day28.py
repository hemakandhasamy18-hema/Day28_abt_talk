import time


# 1. Brute Force Solution
def two_sum_brute_force(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i, j]
    return None


# 2. Optimized Hashing Solution
def two_sum_optimized(numbers, target):
    seen = {}

    for i, num in enumerate(numbers):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return None


# 3. Visualize Hashing Lookup
def visualize_lookup(numbers, target):
    seen = {}

    print("\n🔍 HASHING LOOKUP VISUALIZATION")

    for i, num in enumerate(numbers):
        complement = target - num

        print(f"\nStep {i + 1}:")
        print(f"Current number: {num}")
        print(f"Required complement: {complement}")

        if complement in seen:
            print(f"✅ Complement found at index {seen[complement]}")
            print(f"Treasure pair: [{seen[complement]}, {i}]")
            print(f"Values: [{numbers[seen[complement]]}, {num}]")
            return [seen[complement], i]

        print("❌ Complement not found")
        seen[num] = i
        print("Hash map:", seen)

    print("No matching pair found.")
    return None


# 4. Compare Execution Times
def compare_performance():
    numbers = list(range(1, 3001))
    target = 5999

    start = time.perf_counter()
    brute_result = two_sum_brute_force(numbers, target)
    brute_time = time.perf_counter() - start

    start = time.perf_counter()
    optimized_result = two_sum_optimized(numbers, target)
    optimized_time = time.perf_counter() - start

    print("\n⏱️ PERFORMANCE COMPARISON")
    print("Input size:", len(numbers))
    print(f"Brute Force Time: {brute_time:.6f} seconds")
    print(f"Optimized Time:   {optimized_time:.6f} seconds")
    print("Brute Force Result:", brute_result)
    print("Optimized Result:", optimized_result)

    print("\nTime Complexity:")
    print("Brute Force: O(n²)")
    print("Optimized:   O(n) average")


# 5. Main Program
def main():
    numbers = [2, 7, 11, 15, 3, 6]
    target = 9

    print("=" * 45)
    print("      🏴‍☠️ TREASURE PAIR FINDER")
    print("=" * 45)

    print("Coordinates:", numbers)
    print("Target sum:", target)

    brute_result = two_sum_brute_force(numbers, target)
    optimized_result = two_sum_optimized(numbers, target)

    print("\n🐢 BRUTE FORCE SOLUTION")
    if brute_result is not None:
        print("Indices:", brute_result)
        print("Values:", [numbers[i] for i in brute_result])
    else:
        print("No pair found.")

    print("\n⚡ OPTIMIZED HASHING SOLUTION")
    if optimized_result is not None:
        print("Indices:", optimized_result)
        print("Values:", [numbers[i] for i in optimized_result])
    else:
        print("No pair found.")

    visualize_lookup(numbers, target)
    compare_performance()

    print("\n🏆 Treasure search completed!")


if __name__ == "__main__":
    main()
