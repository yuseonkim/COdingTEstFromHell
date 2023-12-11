//package org.example.Programmers.LV3.코딩테스트공부;
//
//import java.util.ArrayList;
//import java.util.Arrays;
//import java.util.Comparator;
//
//public class Solution {
//
//    public int solution(int alp, int cop, int[][] problems) {
//        //problems = {알고력,코딩력,보상코딩,보상알고,시간}
//        ArrayList<int[]> solved = new ArrayList<>();
//
//        int[] status = {alp,cop};
//        int[][] sortedProblems = Arrays.stream(problems)
//                .sorted((a, b) -> Integer.compare(a[0], b[0]))
//                .toArray(int[][]::new);
//
//        for(int[] problem : sortedProblems){
//            if(canSolved(alp,cop,problem)){
//                solved.add(problem);
//                continue;
//            }
//            int needAlp = problem[0] - alp;
//            int needCop = problem[1] - cop;
//            int oneByOneTime = needAlp+needCop;
//            ArrayList<Integer> solvedGetPointTime = new ArrayList<>();
//            for(int[] solveOne : solved){
//
//            }
//
//        }
//    }
//
//    public boolean canSolved(int alp, int cop, int[] problem){
//        return alp >= problem[0] && cop >= problem[1];
//    }
//
//}
