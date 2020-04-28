//https://leetcode.com/problems/edit-distance/


class Solution {

    func minDistance(_ word1: String, _ word2: String) -> Int {
        if word1.count == 0 && word2.count == 0{ return 0 }
        if word1.count > 0 && word2.count == 0{ return word1.count }
        if word2.count > 0 && word1.count == 0 { return word2.count }

        let word1 = Array(word1)
        let word2 = Array(word2)
        var D = Array.init(repeating: Array.init(repeating: Int.max, count: word2.count + 1), count: word1.count + 1)
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
        return D[word1.count][word2.count]
    }
}

