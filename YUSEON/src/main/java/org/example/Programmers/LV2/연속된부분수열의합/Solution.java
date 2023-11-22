package org.example.Programmers.LV2.연속된부분수열의합;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static int[] solution(int[] sequence, int k) {
        List<Integer> indexs = new ArrayList<>();
        sequence = Arrays.stream(sequence).filter(i -> i <= k).toArray();
        int[] answer = new int[2];
        int sum = 0;
        int saveIndex = 0;
        for (int i = 0; i < sequence.length; i++) {
            System.out.println(i);
            sum += sequence[i];
            indexs.add(i);
            if (sum > k) {
                indexs.clear();
                sum = 0;
                i = saveIndex;
                saveIndex++;
            }
            if (sum == k) {
                answer[0] = indexs.get(0);
                answer[1] = indexs.get(indexs.size()-1);
                indexs.clear();
                sum = 0;
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        int[] sequence = {1, 1, 1, 2, 3, 4, 5};
        int k = 5;
    }
}
