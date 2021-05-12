// https://leetcode.com/problems/the-skyline-problem/

class Solution {
    

     private  class Node implements Comparable<Node>{
        private int x;
        private int height; 
        public Node(int x, int height) {
            this.x = x;
            this.height = height;
        }
        public int compareTo(Node n) {
            if (this.x != n.x) {
                return this.x - n.x;
            }
            else {
                return n.height - this.height;
            }
        }
    }
    
    public  List<List<Integer>>getSkyline(int[][] buildings) {
    	List<List<Integer>> result = new ArrayList<List<Integer>>();
        if (buildings == null || buildings.length == 0) {
            return result;
        }
        List<Node> bds = new LinkedList<Node>();
        
        for (int i = 0; i < buildings.length; i ++) {
            bds.add(new Node(buildings[i][0], buildings[i][2]));
            bds.add(new Node(buildings[i][1], -buildings[i][2]));
        }
        
        Collections.sort(bds);
        PriorityQueue<Integer> q = new PriorityQueue<Integer>(Collections.reverseOrder());
        q.add(0);
        int preHeight = 0;
        for (Node w:bds) {
            if (w.height > 0) {
                q.add(w.height);
            }
            else {
                q.remove((Integer)(-w.height));
            }
            int maxHeight = q.peek();
            if (preHeight != maxHeight) {
            	List<Integer> d0 = new ArrayList<Integer>();
                d0.add(w.x);
                d0.add(maxHeight);
                result.add(d0);
            }
            preHeight = maxHeight;
        }
        return result;
    }
	
    
}