package org.example.Programmers.LV1.붕대감기;

import java.util.HashMap;

public class Solution {
    public static int solution(int[] bandage, int health, int[][] attacks) {
        int firstHealth = health;
        //bandage = [시전 시간, 초당 회복량, 추가 회복량]
        //attack - [공격 시간, 피해량]
        int continuedTime = 0;// 연속 회복 시간
        int lastAttackTime = attacks[attacks.length - 1][0];
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int[] attack : attacks) {
            map.put(attack[0], attack[1]);
        }
        for (int i = 1; i <= lastAttackTime; i++) {
            System.out.println(health);
            if (map.containsKey(i)){
                health -= map.get(i);
                continuedTime = 0;
                if (health <= 0) {
                    return -1;
                }
                continue;
            }
            if(i == 1) {
                continue;
            }
            continuedTime++;
            health+=bandage[1];
            if (continuedTime == bandage[0]) {
                health += bandage[2];
                continuedTime = 0;
            }
            if(health>=firstHealth){
                health = firstHealth;
            }
        }
        return health;
    }

    public static void main(String[] args) {
        int[] bandage = {5,1,5};
        int health = 30;
        int[][] attacks = {{2, 10}, {9, 15}, {10, 5}, {11, 5}};
        System.out.println(solution(bandage,health,attacks));
    }
}
