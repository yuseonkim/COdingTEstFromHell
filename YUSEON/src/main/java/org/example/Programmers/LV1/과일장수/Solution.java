package org.example.Programmers.LV1.과일장수;

import java.util.Arrays;
import java.util.Comparator;
import java.util.stream.IntStream;

public class Solution {
    public static int solution(int k, int m, int[] score) {
        int answer = 0;
        Arrays.sort(score);
        for(int i = score.length - m; i >= 0; i -= m)
            answer += score[i] * m;
        return answer;
    }

    public static void main(String[] args) {
        int k = 4;
        int m = 3;
        int[] score = {4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2};
        solution(k,m,score);
    }

}
