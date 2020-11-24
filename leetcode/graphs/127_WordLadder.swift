class Solution {

    func ladderLength(_ beginWord: String, _ endWord: String, _ wordList: [String]) -> Int {

        // N - wordList size
        //M - beginWord size
        // Time complexity: O(N*M*26)
		//check if endWord exist in wordList
		if !wordList.contains(endWord){ return 0 }

		var result = 1
		//create Set of wordList
		var set = Set<String>()
		for word in wordList {
			set.insert(word)
		}
		//create Q
		var queue = [String]()
		queue.append(beginWord)

		// while Q not empty check for possible combinations for next word
		while !queue.isEmpty{
			let size = queue.count
			for i in 0 ..< size {
				var current = Array(queue.removeFirst())
				for i in 0 ..< current.count {
					let temp = current[i]
					for c in "abcdefghijklmnopqrstuvwxyz"  {
						current[i] = c
						var next = current
						if set.contains(String(next)){
							if String(next) == endWord{
								return result + 1
							}
							queue.append(String(next))
							set.remove(String(next))
						}
					}
				   current[i] = temp
				}
			}
			result += 1
		}
		return 0
    }

}