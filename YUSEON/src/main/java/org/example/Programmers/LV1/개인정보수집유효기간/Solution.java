package org.example.Programmers.LV1.개인정보수집유효기간;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;

public class Solution {

    public static List<Integer> solution(String today, String[] terms, String[] privacies) {
        List<Integer> answer = new ArrayList<>();
        //현재 날짜 일자로 계산
        Long todayNum = dateToDay(today);

        HashMap<String,Long> map = new HashMap<>();
        for(String x : terms){
            String[] arr = x.split(" ");
            map.put(arr[0],Long.parseLong(arr[1])*28);
        }
        for(int i=0;i<privacies.length;i++){
            String[] arr = privacies[i].split(" ");
            if(todayNum - dateToDay(arr[0]) >= map.get(arr[1])){
                answer.add(i+1);
            }
        }

        return answer;
    }

    public static Long dateToDay(String day){
        List<Long> dayLong = Arrays.stream(day.split("\\.")).map(Long::parseLong).collect(Collectors.toList());
        return dayLong.get(0)*12*28 + dayLong.get(1)*28 + dayLong.get(2);
    }

    public static void main(String[] args) {
        String today  = "2022.05.19";
        String[] terms ={"A 6", "B 12", "C 3"};
        String[] privacies = {"2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"};

        List<Integer> a = solution(today,terms,privacies);
        for(Integer i : a){
            System.out.println(i);
        }
    }
}


