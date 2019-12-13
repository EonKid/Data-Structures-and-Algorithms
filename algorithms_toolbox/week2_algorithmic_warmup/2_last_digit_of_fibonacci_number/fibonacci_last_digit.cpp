#include <iostream>

long long get_fibonacci_last_digit_naive(long long n) {
    if (n <= 1)
        return n;

    long long previous = 0;
    long long current  = 1;
    long long result = 0;

    for (long long i = 0; i < n - 1; ++i) {
        result = (previous + current) % 10;
        long long tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;

    }

    return result;
}

int main() {
    long long n;
    std::cin >> n;
    long long c = get_fibonacci_last_digit_naive(n);
    std::cout << c << '\n';
    }
