//package org.example.Programmers.LV2.연속된부분수열의합;
//
//import java.util.ArrayList;
//
//public class Solution {
//    public static int[] solution(int[] sequence, int k) {
//        int start = 0;
//        int end = 0;
//        int sum = sequence[0];
//        int size = 1000000;
//        int[] result = new int[2];
//        ArrayList<int[]> resultList = new ArrayList<>();
//        while (true) {
//            System.out.println(sum + " start : " + start + " end : " + end);
//            if (sum < k) {
//                end++;
//                sum += sequence[end];
//                continue;
//            }
//            if (sum > k) {
//                sum -= sequence[start];
//                start++;
//                continue;
//            }
//            if (sum == k) {
//                if (end - start <= size) {
//                    size = end - start;
//                    result = new int[]{start, end};
//                }
//                if (end == sequence.length - 1) {
//                    sum -= sequence[start];
//                    start++;
//                    continue;
//                }
//                end++;
//                sum += sequence[end];
//            }
//        }
//
//        return result;
//    }
//
//
//    public static void main(String[] args) {
//        int[] sequence = {2, 2, 2, 2, 2};
//        int k = 7;
//        int[] result = solution(sequence, 6);
//        for (int i : result) {
//            System.out.print(i + " ");
//        }
//    }
//}
//
