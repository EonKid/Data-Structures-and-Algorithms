// https://leetcode.com/problems/unique-paths/

/*

---> routes[n][m]
---> routes[0][i] = 1
---> routes[i][0] = 1
---> routes[i][j] = routes[i-1][j] + routes[i][j-1]

*/


class Solution {

    func uniquePaths(_ m: Int, _ n: Int) -> Int {
        var routes = Array.init(repeating: Array.init(repeating: 0, count:m), count: n)

        for j in 0 ..< routes[0].count{
             routes[0][j] = 1
        }

        for i in 0 ..< routes.count{
            routes[i][0] = 1
        }

        for i in 1 ..< routes.count{
            for j in 1 ..< routes[i].count{
                routes[i][j] = routes[i-1][j] + routes[i][j-1]
            }
        }

        return routes[n-1][m-1]
    }

}