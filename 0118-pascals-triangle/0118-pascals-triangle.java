class Solution {
    public List<List<Integer>> generate(int numRows) {       
        List<List<Integer>> result = new LinkedList();
        result.add(List.of(1));      
        for(int i= 1; i < numRows; i++){
        List<Integer> list= new LinkedList();
            list.add(1);
            List<Integer> last = result.get(result.size() - 1);
            int prev = last.get(0);           
            for (int j = 1; j < last.size(); j++) {
                int sum = prev + last.get(j);
                prev = last.get(j);
                list.add(sum);
            }
            list.add(1);
            result.add(list);
        }
        return result;
    }
}