// https://leetcode.com/problems/alien-dictionary/



class Solution{

    func alienOrder(_ words: [String]) -> String{
        if words.count == 0{
            return ""
        }
        var result = ""
        var adjList = [Character: Set<Character>]()
        var queue = [Character]()
        var indegrees = Array.init(repeating: 0, count: 26)

        //create adjacency list
        for word in words{
            let word = Array(word)
            for char in word{
                let currentChar = Character(String(char))
                if adjList[currentChar] == nil{
                    adjList[currentChar] = Set<Character>()
                }
            }
        }

        //find indegree for edges
        for i in 1 ..< words.count{
            let wordIn = Array(words[i])
            let wordOut = Array(words[i-1])

            let minLen = min(wordIn.count, wordOut.count)

            for j in 0 ..< minLen{
                let charIn = Character(String(wordIn[j]))
                let charOut = Character(String(wordOut[j]))

                if charIn != charOut{
                    if !(adjList[charOut]?.contains(charIn))! {
                        let index = Int8(charIn.asciiValue!) - Int8(Character("a").asciiValue!)
                        indegrees[Int(index)] += 1
                        adjList[charOut]?.insert(charIn)
                    }
                    break
                }
            }

        }

        // populate queue
        for (v, _) in adjList{
            let index = Int8(v.asciiValue!) - Int8(Character("a").asciiValue!)
            if indegrees[Int(index)] == 0{
                queue.append(v)
            }
        }

        //run bfs
        while !queue.isEmpty{
            let v = queue.removeFirst()
            result += String(v)
            if let w = adjList[v]{
                for e in w{
                    let index = Int(Int8(e.asciiValue!) - Int8(Character("a").asciiValue!))
                    indegrees[index] -= 1
                    if indegrees[index] == 0{
                         queue.append(e)
                    }
                }
            }
        }

        if adjList.count == result.count {
            return result
        }else{
            return ""
        }
    }

}

let solAlien = Solution()
let words =  ["z","x", "z"]
print("Alien order: \(solAlien.alienOrder(words))")
