// https://leetcode.com/problems/course-schedule-ii/

//Time complexity: O(E+V)
//Space complexity: O(E+V)
class Solution {

    var ordering = [Int]()

        func dfs(_ u: Int,_ adjList:[[Int]],_ visited: inout [Bool],_ recurStack: inout [Bool]) -> Bool{
        visited[u] = true
        recurStack[u] = true

        for v in adjList[u]{
            if !visited[v]{
                if dfs(v,adjList, &visited, &recurStack){
                    return true
                }
            }else if recurStack[v]{
                    return true
            }
        }

        recurStack[u] = false
        ordering.append(u)
        return false
    }

    func acyclic(_ adjList: [[Int]], _ recurStack: inout [Bool]) -> [Int]{
        var visited = Array.init(repeating: false, count: adjList.count)

        for u in 0 ..< adjList.count{
            if !visited[u]{
                if dfs(u, adjList, &visited, &recurStack){
                    return []
                }
            }
        }
        return ordering
    }


    func findOrder(_ numCourses: Int, _ prerequisites: [[Int]]) -> [Int] {
        var adjList = Array.init(repeating: [Int](), count: numCourses)
        var recurStack = Array.init(repeating: false, count:  numCourses)

        for data in prerequisites{
            let u = data[0]
            let v = data[1]
            adjList[u].append(v)
        }

        return acyclic(adjList, &recurStack)
    }
}