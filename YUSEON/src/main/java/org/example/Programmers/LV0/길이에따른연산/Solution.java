package org.example.Programmers.LV0.길이에따른연산;

import java.util.Arrays;

public class Solution {
    static int solution(int[] num_list) {
        if(num_list.length >= 11)
            return Arrays.stream(num_list).sum();
        else {
            final int result = 1;
            return Arrays.stream(num_list).reduce(1,(a,b)->a*b);
        }
    }

    public static void main(String[] args) {
        System.out.println(solution(new int[]{2,3,4,5}));
    }
}
