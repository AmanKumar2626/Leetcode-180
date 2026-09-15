class Solution {
    public void setZeroes(int[][] matrix) {
        
        int c_len = matrix.length;
        int r_len = matrix[0].length;
        int[] row = new int[r_len];
        int[] col = new int[c_len];

        for(int i = 0; i < c_len; i++){
            for(int j =0; j < r_len; j++){
                if(matrix[i][j] == 0)
                {
                    row[j] = 1;
                    col[i] = 1;
                }
            }
        }
        for(int i = 0; i <  c_len; i++){
             if(col[i] == 1){
                for(int j = 0; j <  r_len; j++)              
                    matrix[i][j] = 0; 
             }
        }
        for(int i = 0; i <  r_len; i++){
            if(row[i] == 1){
                for(int j = 0; j <  c_len; j++)
                    matrix[j][i] = 0; 
            }
        }
    }
}