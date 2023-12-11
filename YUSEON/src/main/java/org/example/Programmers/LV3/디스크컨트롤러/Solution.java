package org.example.Programmers.LV3.디스크컨트롤러;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Solution {
    public int solution(int[][] jobs) {
        int[][] sortedJobs = Arrays.stream(jobs).sorted((a, b) -> Integer.compare(a[0], b[0])).toArray(int[][]::new);
        PriorityQueue<int[]> queue = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[1] - o2[1];
            }
        });

        queue.offer(jobs[0]);
        int sum = 0;
        int idx = 1;

        while(!queue.isEmpty()){

        }
    }
}
