package org.example.Programmers.LV2.두큐합같게만들기;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

public class Solution {
    public static int solution(int[] queue1, int[] queue2) {
        Queue<Integer> queue11 = new LinkedList<>();
        Queue<Integer> queue22 = new LinkedList<>();
        long sum1 = 0;
        long sum2 = 0;

        for(int i : queue1){
            queue11.add(i);
            sum1+=i;
        }
        for(int i : queue2){
            queue22.add(i);
            sum2+=i;
        }
        int count = 0;

        for(int i=0;i<queue1.length*4;i++){


            long diff = sum1 - sum2 ;
            if(diff < 0){

                count++;
                int end =  queue22.remove();
                System.out.println("end : "+end);
                queue11.add(end);
                sum1 += end;
                sum2 -= end;
            }
            if(diff > 0){
                count++;
                int end = queue11.remove();
                queue22.add(end);
                sum2 += end;
                sum1 -= end;
            }
            if(diff == 0){
                return count;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        int[] queue1 = {1,2,1,2};
        int[] queue2 = {1,10,1,2};
        System.out.println(solution(queue1,queue2));
    }
}
