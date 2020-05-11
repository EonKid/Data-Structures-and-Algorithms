// https://leetcode.com/problems/word-break/


   class Solution {

	  func iterativeMemo(_ s: [Character], _ dp: inout [Bool], _ wordDict: [String]) -> Bool{
			dp[0] = true
			for i in 0 ..< s.count + 1{
				for j in 0 ..< i{
                    let currentPrefix = String(Array(s[j..<i]))
					if dp[j] && wordDict.contains(currentPrefix){
						dp[i] = true
						break
					   }
				}
			}
			return dp[s.count]
	  }

       func recursiveMemo(_ s: [Character], _ wordSet: Set<String>, _ dp: inout [String: Bool]) -> Bool{
              if dp[String(s)] != nil{
                   return dp[String(s)]!
               }

               if String(s) == ""{
                   return true
               }

               for word in wordSet{
                if s.count >= word.count {
                    let currentWord = String(s[0...(word.count - 1)])
                    if currentWord != word{
                        continue
                    }
                    let nextWord = Array(s[word.count...])
                    if recursiveMemo(nextWord, wordSet, &dp){
                        dp[String(nextWord)] = true
                        return true
                    }
                }
               }
               dp[String(s)] = false
               return false

       }

       func wordBreak(_ s: String, _ wordDict: [String]) -> Bool {

             var dp = [String: Bool]()
             var wordSet = Set<String>()
             for word in wordDict{
               wordSet.insert(word)
             }
              return self.recursiveMemo(Array(s), wordSet, &dp)


			//var dp = Array.init(repeating: false, count: s.count + 1)
			//return iterativeMemo(Array(s), &dp, wordDict)
       }
   }

