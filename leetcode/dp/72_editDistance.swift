//https://leetcode.com/problems/edit-distance/


class Solution {

    var D = [[Int]]()

    func minDistance(_ word1: String, _ word2: String) -> Int {
        if word1.count == 0 && word2.count == 0{ return 0 }
        if word1.count > 0 && word2.count == 0{ return word1.count }
        if word2.count > 0 && word1.count == 0 { return word2.count }

        let word1 = Array(word1)
        let word2 = Array(word2)
        D = Array.init(repeating: Array.init(repeating: Int.max, count: word2.count + 1), count: word1.count + 1)
        for i in 0 ..< word1.count + 1 {
                D[i][0] = i
         }

        for j in 0 ..< word2.count + 1{
             D[0][j] = j
         }

        for i in 1 ..< word1.count + 1{
            for j in 1 ..< word2.count + 1{
                    let insertion = D[i][j - 1] + 1
                    let deletion = D[i-1][j] + 1
                    let match = D[i - 1][j - 1]
                    let mismatch = D[i - 1][j - 1] + 1
                    if word1[i-1] == word2[j-1]{ //compairing previous char
                            D[i][j] = min(insertion, deletion, match)
                    }else{
                            D[i][j] = min(insertion, deletion, mismatch)
                    }

            }
        }
        for data in D{
            print(data)
        }
        return D[word1.count][word2.count]
    }

    func outputAlignment(_ i: Int, _ j: Int){

        if i == 0 && j == 0{
            print("\(i), \(j): \(D[i][j])")
            return
        }
        if i > 0 && D[i][j] == D[i-1][j] + 1{
            print("\(i), \(j): \(D[i][j])")
            self.outputAlignment(i - 1, j)
        }else if j > 0 && D[i][j] == D[i][j - 1] + 1{
            print("\(i), \(j): \(D[i][j])")
            self.outputAlignment(i, j - 1)
        }else {
            print("\(i), \(j): \(D[i][j])")
            outputAlignment(i - 1, j - 1)
        }
    }
}


let sol = Solution()
let word1 = "editing"
let word2 = "distance"
print("edit distance:  \(sol.minDistance(word1, word2))")
print("Print output alignment:")
sol.outputAlignment(word1.count, word2.count)
