/* https://www.geeksforgeeks.org/maximum-profit-sale-wines/
 Price of wines: 2 4 6 2 5
 https://www.youtube.com/watch?v=pwpOC1dph6U
*/


func profit(_ cache: [[Int]], _ begin: Int, _ end: Int,_ wines: [Int])-> Int{
    let N = wines.count
    if begin > end{
        return 0
    }

    if cache[begin][end] != -1{
        return cache[begin][end]
    }
    let winesNotSold = (end - begin + 1)
    let year = N - winesNotSold + 1
    return max(
           profit(cache, begin + 1, end, wines) + year * wines[begin],
           profit(cache, begin, end-1, wines) + year * wines[end]
    )
}

func maximumProfitBySellingWines(_ wines:[Int]) -> Int{
    let cache = Array.init(repeating: Array.init(repeating: -1, count: wines.count), count: wines.count)
    return profit(cache, 0, wines.count - 1, wines)
}


print(maximumProfitBySellingWines([2, 4, 6, 2, 5]))
