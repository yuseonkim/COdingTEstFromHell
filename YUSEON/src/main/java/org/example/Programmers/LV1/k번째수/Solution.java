package org.example.Programmers.LV1.k번째수;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static int[]  solution(int[] array,int[][] commands){
        int[] answer = new int[commands.length];
        for(int i=0;i<commands.length;i++){
            answer[i] = cut(array,commands[i]);
        }
        return answer;
    }

    public static int cut(int[] array, int[] command){
        int start = command[0]-1; // 2
        int end = command[1]; // 5
        int num = command[2];
        int[] arr = Arrays.stream(array,start,end).sorted().toArray();
        return Arrays.stream(array,start,end).sorted().toArray()[num-1];
    }

    public static void main(String[] args) {
        int[] array = {1,5,2,6,3,7,4};
        int[][] commands = {{2,5,3},{4,4,1},{1,7,3}};
        int[] answer =  solution(array,commands);
        for(int i=0;i<answer.length;i++){
            System.out.println(answer[i]);
        }
    }

    public Solution() {
    }
}
