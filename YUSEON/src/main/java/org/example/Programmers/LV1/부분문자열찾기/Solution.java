package org.example.Programmers.LV1.부분문자열찾기;

class Solution {
    public int solution(String t, String p) {
        int count = 0;
        int length = p.length();
        for(int i=0;i<t.length()-length+1;i++){
            StringBuilder slicedT = new StringBuilder();
            for(int j=0;j<length;j++){
                slicedT.append(t.charAt(i+j));
            }
            Long slicedANum = Long.parseLong(String.valueOf(slicedT));
            if(slicedANum <= Long.parseLong(p)){
                count++;
            }
        }
        return count;
    }
}
