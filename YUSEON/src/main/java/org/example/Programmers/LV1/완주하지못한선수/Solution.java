package org.example.Programmers.LV1.완주하지못한선수;

import java.util.Arrays;
import java.util.stream.Collectors;

public class Solution {
    public String solution(String[] participant, String[] completion) {
        return Arrays.stream(participant).filter(i -> !Arrays.asList(completion).contains(i)).collect(Collectors.toList()).get(0);
    }
}
