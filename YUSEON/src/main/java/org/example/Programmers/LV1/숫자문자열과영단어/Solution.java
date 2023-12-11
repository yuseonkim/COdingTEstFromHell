package org.example.Programmers.LV1.숫자문자열과영단어;

import java.util.HashMap;

public class Solution {
    public int solution(String s) {

        HashMap<String,Integer> map = new HashMap<>();
        map.put("zero",0);
        map.put("one",1);
        map.put("two",2);
        map.put("three",3);
        map.put("four",4);
        map.put("five",5);
        map.put("six",6);
        map.put("seven",7);
        map.put("eight",8);
        map.put("nine",9);

        for(String key : map.keySet()){
            if(s.contains(key)){
                s = s.replaceAll(key, String.valueOf(map.get(key)));
            }
        }

        return Integer.parseInt(s);

    }
}
