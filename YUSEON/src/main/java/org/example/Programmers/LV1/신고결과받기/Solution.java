package org.example.Programmers.LV1.신고결과받기;

import java.util.*;
import java.util.stream.Collectors;

public class Solution {


    public int[] solution(String[] id_list, String[] reports, int k) {
        HashMap<String,Integer> map = new HashMap<>();
        // 아이디를 map에 넣어주기 -> 신고 개수 작성할 것 O(n)
        for(String id : id_list){
            map.put(id,0);
        }
        // 신고자 피신고자 중복 쌍 set으로 처리
        HashSet<String> set = new HashSet<>(Arrays.asList(reports));
        for(String report : set) {
            String[] split = report.split(" ");
            String reported = split[1];
            map.replace(reported, map.get(reported) + 1);
        }
        ArrayList<String> result = new ArrayList<>();
        for(String id : id_list){
            if(map.get(id) >= k){
                result.add(id);
            }
        }
        List<String> reportResult =set.stream()
                .filter(str -> {
                    String[] parts = str.split(" ");
                    return parts.length > 1 && result.contains(parts[parts.length - 1]);
                })
                .map(str -> str.split(" ")[0])
                .collect(Collectors.toList());

        int[] answer = new int[id_list.length];
        for(int i =0;i<answer.length;i++){
            answer[i] = 0;
        }
        for(String a : reportResult){
            for(int i=0;i<id_list.length;i++){
                if(a.equals(id_list[i]))
                    answer[i]++;
            }

        }
        return  answer;


    }
    public static void main(String[] args) {

    }
}
