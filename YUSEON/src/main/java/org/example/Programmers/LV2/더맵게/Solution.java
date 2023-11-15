package org.example.Programmers.LV2.더맵게;

import java.util.PriorityQueue;
import java.util.stream.IntStream;

public class Solution {
    public static int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        IntStream.of(scoville).forEach(heap::add);
        while(true) {
            if(heap.size()<=1 && heap.stream().allMatch(i -> i< K)){
                return -1;
            }
            if(heap.stream().allMatch(i -> i>= K)){
                break;
            }
            answer++;
            int newNum = heap.remove() +heap.remove()*2;
            heap.add(newNum);

        }
        return answer;
    }

    public static void main(String[] args) {
        int[] scoville =  {1,2,3,9,10,12};
        System.out.println(solution(scoville,7));
    }
}
